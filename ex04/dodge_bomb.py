import pygame as pg
import sys

def main():
    clock = pg.time.Clock()
    
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    
    back_sfc = pg.image.load("fig/pg_bg.jpg")

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
