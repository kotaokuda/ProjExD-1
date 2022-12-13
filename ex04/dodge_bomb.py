import pygame as pg
import sys
import random
import time

class bomb: #爆弾を作成するクラス
    def __init__(self, scr_sfc, scr_rct):
        self.bomb_sfc = pg.Surface((20, 20))
        pg.draw.circle(self.bomb_sfc, "red", (10,10), 10)
        self.bomb_rct = self.bomb_sfc.get_rect()
        self.bx = random.randint(0, scr_rct.width)
        self.by = random.randint(0, scr_rct.height)
        self.bomb_sfc.set_colorkey("black")
        scr_sfc.blit(self.bomb_sfc, (self.bx, self.by))
        self.spd = 2
        self.vx = +self.spd
        self.vy = +self.spd
        self.tmr = 0
        print(self.bomb_rct.center)
        print(self.bx, self.by)
    
    def Update(self): #爆弾のスピードを制御する
        self.tmr += 1
        if self.tmr%1000:
            self.spd = 2 + self.tmr//2000
        if self.vx < 0:
            self.vx = -self.spd
        else:
            self.vx = +self.spd
        if self.vy < 0:
            self.vy = -self.spd
        else:
            self.vy = +self.spd

def check_bound(obj_rct, scr_rct): #要素が画面の外に行かないか確認する
    x, y = +1, +1
    if obj_rct.left < scr_rct.left or obj_rct.right > scr_rct.right:
        x = -1
    if obj_rct.top < scr_rct.top or obj_rct.bottom > scr_rct.bottom:
        y = -1
    return x, y

def check_tori(obj_rct, scr_rct, int): #こうかとんが画面外に出たときの処理を行う
    tx, ty = check_bound(obj_rct, scr_rct)
    if tx == -1:
        obj_rct.centerx += -1*int
    if ty == -1:
        obj_rct.centery += -1*int

# def popitem(tmr): #アイテムを出したかった残骸
#     global scrn_sfc, scrn_rct
#     if tmr%10000 == 0:
#         item_sfc = pg.Surface((20, 20))
#         item_rct = item_sfc.get_rect()
#         pg.draw.circle(item_sfc, "red", (10,10), 10)
#         bx = random.randint(0, scrn_rct.width)
#         by = random.randint(0, scrn_rct.height)
#         item_sfc.set_colorkey("black")
#         scrn_sfc.blit(item_sfc, (bx, by))
        

def main():
    tori_spd = 3 #こうかとんのスピード
    tmr = 0 #時間計測
    bgn = time.time() #プレイ時間計測
    clock = pg.time.Clock()
    
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()
    back_sfc = pg.image.load("fig/pg_bg.jpg")
    back_rct = back_sfc.get_rect()
    back_rct.center = 800, 450
    scrn_sfc.blit(back_sfc, back_rct)

    tori_sfc = pg.image.load("fig/3.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 1.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct)

    # bomb_sfc = pg.Surface((20, 20))
    # bomb_rct = bomb_sfc.get_rect()
    # pg.draw.circle(bomb_sfc, "red", (10,10), 10)
    # bx = random.randint(0, scrn_rct.width)
    # by = random.randint(0, scrn_rct.height)
    # bomb_sfc.set_colorkey("black")
    # scrn_sfc.blit(bomb_sfc, (bx, by))
    bombs = []
    bombs.append(bomb(scrn_sfc, scrn_rct))

    playtime = pg.font.Font(None, 40)
    now = time.time()
    txt = playtime.render(f"{now-bgn:.01f}s", True, "black")
    scrn_sfc.blit(txt, (scrn_rct.width-60, 10))
    
    pg.display.update()
    
    while True:
        scrn_sfc.blit(back_sfc, back_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]: 
            tori_rct.centery -= tori_spd
            check_tori(tori_rct,scrn_rct, -tori_spd)
        if key_lst[pg.K_DOWN]:
            tori_rct.centery += tori_spd
            check_tori(tori_rct,scrn_rct, tori_spd)
        if key_lst[pg.K_LEFT]:
            tori_rct.centerx -= tori_spd
            check_tori(tori_rct,scrn_rct, -tori_spd)
        if key_lst[pg.K_RIGHT]: 
            tori_rct.centerx += tori_spd
            check_tori(tori_rct,scrn_rct, tori_spd)

        scrn_sfc.blit(tori_sfc, tori_rct)
        for b in bombs:
            b.bomb_rct.move_ip(b.vx, b.vy)
            x, y = check_bound(b.bomb_rct, scrn_rct)
            b.vx *= x
            b.vy *= y
            scrn_sfc.blit(b.bomb_sfc, b.bomb_rct)
            b.Update()
            if tori_rct.colliderect(b.bomb_rct):
                return "GAME OVER"
        if tmr%1000 == 0: #爆弾を定期的に追加
            bombs.append(bomb(scrn_sfc,scrn_rct))
            print("+")
            

        now = time.time()
        txt = playtime.render(f"{now-bgn:.01f}s", True, "black")
        scrn_sfc.blit(txt, (scrn_rct.width-100, 10))

        pg.display.update()
        clock.tick(1000)
        tmr += 1

if __name__ == "__main__":
    pg.init()
    print(main())
    pg.quit()
    sys.exit()
