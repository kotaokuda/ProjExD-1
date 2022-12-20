import pygame as pg
import random
import sys


key_delta = {
    pg.K_UP:    [0, -1],
    pg.K_DOWN:  [0, +1],
    pg.K_LEFT:  [-1, 0],
    pg.K_RIGHT: [+1, 0],
}


class Screen:
    def __init__(self, title, whtpl, bgfile):
        self.title = title
        self.whtpl = whtpl
        pg.display.set_caption(self.title)
        self.sfc = pg.display.set_mode(self.whtpl)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgfile)
        self.bgi_rct = self.bgi_sfc.get_rect()
 
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0], }

    def __init__(self, figfile, zoom, center):
        self.sfc = pg.image.load(figfile)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.center = center


def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    clock =pg.time.Clock()
    # 練習１
    # pg.display.set_caption("逃げろ！こうかとん")
    # scrn_sfc = pg.display.set_mode((1600, 900))
    # scrn_rct = scrn_sfc.get_rect()
    # pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    # pgbg_rct = pgbg_sfc.get_rect()
    sc = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    sc.blit()

    # 練習３
    # tori_sfc = pg.image.load("fig/6.png")
    # tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    # tori_rct = tori_sfc.get_rect()
    # tori_rct.center = 900, 400
    # # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    # sc.sfc.blit(tori_sfc, tori_rct) 
    tori = Bird("fig/6.png", 2.0, (900, 400))

    # 練習５
    bomb_sfc = pg.Surface((20, 20)) # 正方形の空のSurface
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, sc.rct.width)
    bomb_rct.centery = random.randint(0, sc.rct.height)
    sc.sfc.blit(bomb_sfc, bomb_rct) 
    vx, vy = +1, +1

    # 練習２
    while True:
        sc.sfc.blit(sc.bgi_sfc, sc.bgi_rct) 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_dct = pg.key.get_pressed()
        for key, delta in key_delta.items():
            if key_dct[key]:
                tori.rct.centerx += delta[0]
                tori.rct.centery += delta[1]
            # 練習7
            if check_bound(tori.rct, sc.rct) != (+1, +1):
                tori.rct.centerx -= delta[0]
                tori.rct.centery -= delta[1]
        sc.sfc.blit(tori.sfc, tori.rct) # 練習3

        # 練習６
        bomb_rct.move_ip(vx, vy)
        sc.sfc.blit(bomb_sfc, bomb_rct) 
        yoko, tate = check_bound(bomb_rct, sc.rct)
        vx *= yoko
        vy *= tate

        # 練習８
        if tori.rct.colliderect(bomb_rct):
            return

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init() # 初期化
    main() # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()