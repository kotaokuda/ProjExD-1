import pygame as pg
import sys

def main():
    clock = pg.time.Clock()
    
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    
    back_sfc = pg.image.load("fig/pg_bg.jpg")
    back_rct = back_sfc.get_rect()
    back_rct.center = 800, 450
    scrn_sfc.blit(back_sfc, back_rct)

    pg.display.update()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
