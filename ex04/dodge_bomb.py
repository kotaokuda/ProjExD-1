import pygame as pg
import sys
import random

def check_bound(obj_rct, scr_rct):
    x, y = +1, +1
    if obj_rct.left < scr_rct.left or obj_rct.right > scr_rct.right:
        x = -1
    if obj_rct.top < scr_rct.top or obj_rct.bottom > scr_rct.bottom:
        y = -1
    return x, y

def check_tori(obj_rct, scr_rct, int):
    tx, ty = check_bound(obj_rct, scr_rct)
    if tx == -1:
        obj_rct.centerx += -1*int
    if ty == -1:
        obj_rct.centery += -1*int

def main():
    tori_spd = 2
    bomb_spd = 2

    clock = pg.time.Clock()
    
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()
    back_sfc = pg.image.load("fig/pg_bg.jpg")
    back_rct = back_sfc.get_rect()
    back_rct.center = 800, 450
    scrn_sfc.blit(back_sfc, back_rct)

    tori_sfc = pg.image.load("fig/3.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct)

    bomb_sfc = pg.Surface((20, 20))
    bomb_rct = bomb_sfc.get_rect()
    pg.draw.circle(bomb_sfc, "red", (10,10), 10)
    bx = random.randint(0, scrn_rct.width)
    by = random.randint(0, scrn_rct.height)
    bomb_sfc.set_colorkey("black")
    scrn_sfc.blit(bomb_sfc, (bx, by))

    pg.display.update()

    vx, vy = +bomb_spd, +bomb_spd
    
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

        bomb_rct.move_ip(vx, vy)
        x, y = check_bound(bomb_rct, scrn_rct)
        vx *= x
        vy *= y
        scrn_sfc.blit(bomb_sfc, bomb_rct)
        
        if tori_rct.colliderect(bomb_rct):
            return "GAME OVER"

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
