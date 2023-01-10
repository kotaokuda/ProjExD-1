import pygame as pg
import random
import sys
import os


class Screen:#背景
    def __init__(self, title, whtpl, bgfile):
        self.title = title
        self.whtpl = whtpl
        pg.display.set_caption(self.title)
        self.sfc = pg.display.set_mode(self.whtpl)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgfile)
        self.bgi_rct = self.bgi_sfc.get_rect()
 
    def blit(self): #出力
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:#こうかとん
    def __init__(self, figfile, zoom, center,sp):
        self.sfc = pg.image.load(figfile)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom)
        self.sfc = pg.transform.flip(self.sfc, True, False) #向きを反転
        self.rct = self.sfc.get_rect()
        self.rct.center = center
        self.sp = sp    
        self.kis = False

    def blit(self, scr): #出力
        scr.sfc.blit(self.sfc, self.rct)

    #スペースを押したときにこうかとんが跳ねる関数（c0a21166が改良）
    def update(self, scr):
        key_dct = pg.key.get_pressed()
        if key_dct[pg.K_SPACE] and self.kis == False: #加速度決め（連続押しは不可）
            self.kis =True
            self.sp = -4
        else:
            self.sp += 0.1
            if self.sp > 5:
                self.sp = 5
        if not key_dct[pg.K_SPACE]: #スペースを押してないときに跳ねる機構を回復
            self.kis = False
        self.rct.centery += self.sp
        if self.rct.top < scr.rct.top: #天井を叩いたとき、画面外に行かない処理
            self.rct.centery += scr.rct.top - self.rct.top 
        scr.sfc.blit(self.sfc, self.rct) #書き込み


class Wall:#壁
    def __init__(self):
        self.top = random.randint(0, 6)
        self.sfc1 = pg.Surface((100, self.top * 100))
        self.sfc1.set_colorkey((0, 0, 0))
        self.sfc2 = pg.Surface((100, 600 - self.top * 100))
        self.sfc2.set_colorkey((0, 0, 0))
        pg.draw.rect(self.sfc1, (0, 128, 0), (0, 0, 100, self.top * 100), 0)
        pg.draw.rect(self.sfc2, (0, 255, 255), (0, 0, 100, 600 - self.top * 100), 0)
        self.rct1 = self.sfc1.get_rect()
        self.rct1.center = (1550, self.top * 50)
        self.rct2 = self.sfc2.get_rect() 
        self.rct2.center = (1550, 600 + self.top * 50)

    def blit(self, scr):
        scr.sfc.blit(self.sfc1, self.rct1)
        scr.sfc.blit(self.sfc2, self.rct2)

    def update(self, scr): #位置の移動
        self.rct1.move_ip(-1, 0)
        self.rct2.move_ip(-1, 0)
        self.blit(scr)


#スコアをテキストファイルに記入する関数（c0a21166が作成）
def score():
    score = str(pg.time.get_ticks() / 1000)
    if os.path.exists("score.txt") == False:
        with open("score.txt","w",encoding="utf_8") as f:
            f.write(score)
    else:
        with open("score.txt","r",encoding="utf_8") as f:
            line = f.read()
            if float(line) < float(score):
                with open("score.txt","w",encoding="utf_8") as f:
                    f.write(score)


#メイン
def main():
    global game
    time = 0

    clock =pg.time.Clock()

    scr = Screen("飛べ！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    scr.blit()

    kkt = Bird("fig/3.png", 2.0, (scr.whtpl[0]/2, scr.whtpl[1]/2),0)
    kkt.blit(scr)

    wlls = [Wall()]
    wlls[0].blit(scr)

    while True:
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game = False
                return

        kkt.update(scr)

        if time % 700 == 699:
                wlls.append(Wall())

        for wll in wlls:
            wll.update(scr)
            if wll.rct1.right < 0:
                wlls.remove(wll)

            if kkt.rct.colliderect(wll.rct1) or kkt.rct.colliderect(wll.rct2):
                score() 
                return
        
        if kkt.rct.bottom > scr.rct.bottom:
            score()
            return
    
        pg.display.update()
        time += 1
        clock.tick(1000)
    

#本体
if __name__ == "__main__":
    game = True
    pg.init() # 初期化
    main() # ゲームの本体
    #pg.time.wait(1000) #テスト時にスペース連打でコードがぐちゃぐちゃになるのをケア
    pg.quit() # 初期化の解除
    sys.exit()