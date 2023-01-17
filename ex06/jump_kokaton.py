import pygame as pg
import pygame
import random
import time #鍵和田崇允：追加部分
import sys
import os


class Screen:#背景を生成
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
        self.images = []   #C0A21169 山内利功
        self.index = 0
        for num in range(1, 4):
            img = pygame.image.load(f"fig/{num}.png")
            self.images.append(img)
        self.index = random.randint(0, 2)
        self.sfc =  self.images[self.index] # インデックスを用いて画像を取得
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom)
        self.sfc = pg.transform.flip(self.sfc, True, False) #向きを反転
        self.rct = self.sfc.get_rect()
        self.rct.center = center
        self.sp = sp    
        self.kis = False
        self.arrive_time = time.time()  #鍵和田崇允：追加部分　時間の計測用、なぜかメイン関数内で処理できなかったのでこちらで代用

    def timecount(self):  #鍵和田崇允：追加部分　生存時間を返す
        time_dead = time.time()
        time_str = str(round(time_dead - self.arrive_time, 1))
        return time_str

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
        self.pass_sitayo = True #鍵和田崇允：追加部分（点数計算が重複しないようにするフラグ）

    def blit(self, scr):
        scr.sfc.blit(self.sfc1, self.rct1)
        scr.sfc.blit(self.sfc2, self.rct2)

    def update(self, scr): #位置の移動
        self.rct1.move_ip(-1, 0)
        self.rct2.move_ip(-1, 0)
        self.blit(scr)

class Button:#ボタン用imageの生成 C0A21081作成
    def __init__(self, figfile, center):
        self.sfc = pg.image.load(figfile)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 2)
        self.sfc = pg.transform.flip(self.sfc, True, False) #向きを反転
        self.rct = self.sfc.get_rect()
        self.rct.center = center

    def blit(self, scr):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr):
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
    Start = True
    score = 0 #鍵和田崇允：追加部分　壁を越えた回数
    clock =pg.time.Clock()

    index = 0       #ゲームの進行を管理する変数
    
    scr = Screen("飛べ！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    scr.blit()

    kbn_start = Button("fig/3.png", (400, 450))#スタートボタンを生成
    kbn_start.blit(scr)
    kbn_exit = Button("fig/2.png", (1200, 450))#終了ボタンを生成
    kbn_exit.blit(scr)
    start = pg.font.Font(None, 100)
    exit = pg.font.Font(None, 100)
    txt_s = start.render("START", True, "black")
    txt_e = exit.render("EXIT", True, "black")
    scr.sfc.blit(txt_s, (kbn_start.rct.width, kbn_start.rct.height)) 
    scr.sfc.blit(txt_e, (kbn_exit.rct.width, kbn_exit.rct.height)) 


    while Start:
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game = False
                return
            elif event.type == pg.MOUSEBUTTONUP:
                posx, posy = event.pos
                if kbn_start.rct.left < posx and posx < kbn_start.rct.right:
                    if kbn_start.rct.bottom > posy and posy > kbn_start.rct.top:#画像範囲内をクリックしたら反応
                        Start =False#スタート画面のwhileを脱出
                elif kbn_exit.rct.left < posx and posx < kbn_exit.rct.right:
                    if kbn_exit.rct.bottom > posy and posy > kbn_exit.rct.top:#画像範囲内をクリックしたら反応
                        game = False
                        return


        kbn_start.update(scr)
        kbn_exit.update(scr)

        txt_s = start.render("START", True, "black")
        txt_e = exit.render("EXIT", True, "black")
        scr.sfc.blit(txt_s, (kbn_start.rct.centerx - 100, kbn_start.rct.centery + 50)) 
        scr.sfc.blit(txt_e, (kbn_exit.rct.centerx - 100, kbn_exit.rct.centery + 50)) 

        pg.display.update() #C0A21081作成↑

    kkt = Bird("fig/3.png", 2.0, (scr.whtpl[0]/2, scr.whtpl[1]/2),0)
    kkt.blit(scr)

    wlls = [Wall()]
    wlls[0].blit(scr)

    font1 = pg.font.Font(None, 200)     #テキストのフォントおよびサイズの設定
    font2 = pg.font.Font(None, 100)     #テキストのフォントおよびサイズの設定

    while True:
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game = False
                return

            if event.type == pg.KEYDOWN:                                    #キーが押されたとき
                if index == 1:                                              #indexが1の時
                    if event.key == pg.K_x:                                 #押されたキーがxの時
                        game = False                                        #gameをFalseにする
                        return                                              #main関数を抜ける
                    if event.key == pg.K_r:                                 #押されたキーがrの時
                        index = 0                                           #indexを0にする
                        score = 0
                        kkt.rct.center = (scr.whtpl[0]/2, scr.whtpl[1]/2)   #こうかとんの位置を初期化する
                        wlls = [Wall()]                                     #壁をリセットする
                        time = 0                                            #タイマーをリセットする
                        pg.display.update()                                 #ディスプレイを更新する
        
        if index == 0:      #indexが0の時

            kkt.update(scr)

            if time % 700 == 699:
                    wlls.append(Wall())

            for wll in wlls:
                wll.update(scr)
                if kkt.rct.centerx > wll.rct1.right and wll.pass_sitayo:   #鍵和田崇允：追加部分（ここから下2行）　スコアを増やす
                  score += 1
                  wll.pass_sitayo = False #重複計算回避
                if wll.rct1.right < 0:
                    wlls.remove(wll)

                if kkt.rct.colliderect(wll.rct1) or kkt.rct.colliderect(wll.rct2):
                    # score() #西山 
                    index = 1 #奥田
            
            if kkt.rct.bottom > scr.rct.bottom:
                # score() #西山
                index = 1
        
            
            #鍵和田崇允：追加部分 時間表示+スコア表示
            fonto = pg.font.Font(None, 80)
            time_str = fonto.render("Time:"+kkt.timecount(), True, (0, 0, 0))
            scr.sfc.blit(time_str, (1300, 0))
            score_str = fonto.render("Score:"+str(score), True, (0, 0, 0))
            scr.sfc.blit(score_str, (1000, 0))
            pg.display.update()
            time += 1

            if index == 1:      #indexが1の時 #奥田

                text1 = font1.render("GAME OVER!", True, (255, 0, 0))                   #メッセージの文字、滑らかにするかを指定、色を指定
                text2 = font2.render("Finish [X] Restart [R]", True, (255, 255, 255))   #メッセージの文字、滑らかにするかを指定、色を指定
                scr.sfc.blit(text1, (350, 300))                                         #メッセージと、場所を指定して表示
                scr.sfc.blit(text2, (450, 500))                                         #メッセージと、場所を指定して表示

                pg.display.update()     #画面を更新する

        clock.tick(1000)
    

#本体
if __name__ == "__main__":
    game = True
    pg.init() # 初期化
    main() # ゲームの本体
    pg.quit() # 初期化の解除
    score()
    sys.exit()