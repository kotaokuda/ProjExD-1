import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock()
    
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    
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
    pg.draw.circle(bomb_sfc, "red", (10,10), 10)
    bx = random.randint(0, scrn_sfc.get_width())
    by = random.randint(0, scrn_sfc.get_height())
    bomb_sfc.set_colorkey("black")
    scrn_sfc.blit(bomb_sfc, (bx, by))

    pg.display.update()

    while True:
        scrn_sfc.blit(back_sfc, back_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]: 
            tori_rct.centery -= 1
        if key_lst[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_lst[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_lst[pg.K_RIGHT]: 
            tori_rct.centerx += 1
        scrn_sfc.blit(tori_sfc, tori_rct)

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
