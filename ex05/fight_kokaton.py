import pygame as pg
import random
import sys
import time
                            

class Screen:
    """
    スクリーンを作るためのクラス
    """
    def __init__(self, title, whtpl, bgfile):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(whtpl) #スクリーンサイズを指定
        self.rct = self.sfc.get_rect() #スクリーンオブジェクトのrectを取得
        self.bgi_sfc = pg.image.load(bgfile) #背景画像を読み込む
        self.bgi_rct = self.bgi_sfc.get_rect() #背景画像オブジェクトのrectを取得
 
    def blit(self): #スクリーンに画像を貼り付け
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    """
    １Pこうかとんを作るためのクラス
    """
    key_delta = {
        pg.K_UP:    [0, -2],
        pg.K_DOWN:  [0, +2],
        pg.K_LEFT:  [-2, 0],
        pg.K_RIGHT: [+2, 0], } #入力キー毎の進む速度を指定

    def __init__(self, figfile, zoom, center):
        self.sfc = pg.image.load(figfile) #こうかとん画像を読み込み
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom) #こうかとんのサイズを変更
        self.rct = self.sfc.get_rect() #こうかとんオブジェクトのrectを取得
        self.rct.center = center #こうかとんの位置を指定
        self.status = "normal" #こうかとんの状態を指定
        self.title = "1P" #こうかとんの名前を指定
        self.time = 0 #こうかとんのステータス強化時間

    def blit(self, scr):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr):
        key_dct = pg.key.get_pressed()
        for key, delta in self.key_delta.items(): #入力キーに応じてこうかとんを動かす
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]

            if check_bound(self.rct, scr.rct) != (+1, +1): #画面外に出ないか確認する。出ていたら画面内に戻す
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        scr.sfc.blit(self.sfc, self.rct)

        if self.status != "normal": #statusの継続時間を測る
            self.time += 1
            if self.time > 4000: #4000たったらstatus効果を打ち消し
                self.status = "normal"
                self.time = 0

    def change_status(self, stauts): #ステータスを変更
        self.status = stauts


class Bird2p:
    """
    2Pこうかとんを作るためのクラス
    """
    key_delta = {
        pg.K_w:    [0, -2],
        pg.K_s:  [0, +2],
        pg.K_a:  [-2, 0],
        pg.K_d: [+2, 0], } #入力キー毎の進む速度を指定

    def __init__(self, figfile, zoom, center):
        self.sfc = pg.image.load(figfile) #こうかとん画像を読み込み
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom) #こうかとんのサイズを変更
        self.rct = self.sfc.get_rect() #こうかとんオブジェクトのrectを取得
        self.rct.center = center #こうかとんの位置を指定
        self.status = "normal" #こうかとんの状態を指定
        self.title = "2P" #こうかとんの名前を指定
        self.time =0 #こうかとんのステータス強化時間

    def blit(self, scr):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr):
        key_dct = pg.key.get_pressed()
        for key, delta in self.key_delta.items(): #入力キーに応じてこうかとんを動かす
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]

            if check_bound(self.rct, scr.rct) != (+1, +1): #画面外に出ないか確認する。出ていたら画面内に戻す
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        scr.sfc.blit(self.sfc, self.rct) 

        if self.status != "normal": #statusの継続時間を測る
            self.time += 1
            if self.time > 4000: #4000たったらstatus効果を打ち消し
                self.status = "normal"
                self.time = 0

    def change_status(self, stauts): #ステータスを変更
        self.status = stauts
        print(self.status)


class Bomb:
    """
    爆弾を作るためのクラス
    """
    def __init__(self, colortpl, radius, speedtpl, scr):
        self.sfc = pg.Surface((20, 20)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0)) #黒色の背景を削除
        pg.draw.circle(self.sfc, colortpl, (radius, radius), radius) #爆弾の図形を作る
        self.rct = self.sfc.get_rect() #爆弾オブジェクトのrectを取得
        inx = random.randint(0, scr.rct.width) #爆弾の初期座標をランダムで指定
        iny = random.randint(0, scr.rct.height)
        self.rct.centerx = inx 
        self.rct.centery = iny
        scr.sfc.blit(self.sfc, self.rct) #スクリーンに貼り付け
        self.vx, self.vy = speedtpl #爆弾の移動方向を指定
        self.time = 0 #爆弾ごとの時間
        self.speed = 1 #爆弾の速度

    def blit(self, scr): #スクリーンに貼り付け
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr): #爆弾を動かす
        self.rct.move_ip(self.vx * self.speed, self.vy * self.speed) #爆弾を動かす
        scr.sfc.blit(self.sfc, self.rct) 
        yoko, tate = check_bound(self.rct, scr.rct) #壁に当たったら反転する
        self.vx *= yoko
        self.vy *= tate
        self.time += 1
        if self.time % 10000: #10000毎にスピードを微増
            self.speed += 0.0001


class Item:
    """
    アイテムを作るためのクラス
    """
    def __init__(self, title, figfile, zoom, scr):
        self.sfc = pg.image.load(figfile) #アイテム画像を読み込み
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom) #アイテム画像の大きさを調整
        self.rct = self.sfc.get_rect() #アイテムオブジェクトのrectを取得
        inx = random.randint(0, scr.rct.width) #アイテムの出現位置を決定
        iny = random.randint(0, scr.rct.height)
        self.rct.centerx = inx
        self.rct.centery = iny
        scr.sfc.blit(self.sfc, self.rct) #スクリーンに貼り付け
        self.title = title #アイテム名
        self.time = 0 #アイテム出現時間
    
    def update(self, scr):
        scr.sfc.blit(self.sfc, self.rct)
        self.time += 1

    def item_power(self, ttb): #statusを変更
        if self.title == "suter":
            ttb.change_status("suter") #一回目に直接変えたら上手くいかなかったので関数を呼び出してステータスを変更しているが、たぶん直接変えても大丈夫なはず。
        elif self.title == "shield":
            ttb.change_status("shield")


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
    tim = 0 #int時間を計測
    bgn = time.time() #開始時間を計測
    ttlst = [] #こうかとんのリスト
    bombs = [] #爆弾のリスト
    on_items = [] #画面上にあるアイテムのリスト
    true = True #ゲーム画面に居続けるためのbool
    loser = ""

    clock =pg.time.Clock()

    scr = Screen("戦え！こうかとん", (1600, 900), "fig/pg_bg.jpg") #Screenインスタンスを生成
    scr.blit()

    ttlst.append(Bird("fig/6.png", 1.0, (1350, 400)))
    ttlst[0].blit(scr)
    ttlst.append(Bird2p("fig/2.png", 1.0, (450, 400)))
    ttlst[1].blit(scr)

    vx = random.choice([-1, +1])
    vy = random.choice([-1, +1])
    bombs.append(Bomb("red", 10, (vx, vy), scr))

    playtime = pg.font.Font(None, 40)
    now = time.time()
    txt = playtime.render(f"{now-bgn:.01f}s", True, "black") #プレイ時間を表示
    scr.sfc.blit(txt, (10, scr.rct.height - 5)) 

    items = [("super", "fig/star-1.png", 0.1), ("shield", "fig/shield.png", 0.05)] #アイテムのリスト
    on_items = []

    while true:
        scr.blit()

        for event in pg.event.get(): #ゲームの終了
            if event.type == pg.QUIT:
                return
        
        for ttb in ttlst:
            ttb.update(scr)

        if tim % 1000 == 0: #一定時間ごとに爆弾を追加
            vx = random.choice([-1, +1])
            vy = random.choice([-1, +1])
            bombs.append(Bomb("red", 10, (vx, vy), scr))

        if tim % 10000 == 9999: #一定時間ごとにアイテムが出現
            item = random.choice(items)
            on_items.append(Item(item[0], item[1], item[2], scr))

        for itm in on_items: #アイテムをゲットしたか確認
            itm.update(scr)
            for ttb in ttlst:
                if ttb.rct.colliderect(itm.rct):
                    itm.item_power(ttb)
                    on_items.remove(itm)

        for bom in bombs: #爆弾に衝突したか確認
            bom.update(scr)

            for ttb in ttlst:
                if ttb.rct.colliderect(bom.rct):
                    if ttb.status == "normal": #ノーマル時に衝突ならゲームオーバー
                        loser = ttb.title
                        true = False
                    elif ttb.status == "shield": #シールド時に衝突ならはじく
                        bom.vx *= -1
                        bom.vy *= -1
                    elif ttb.status == "suter": #スター時に衝突なら破壊
                        bombs.remove(bom)

        now = time.time()
        txt = playtime.render(f"{now-bgn:.01f}s", True, "black") #プレイ時間を表示
        scr.sfc.blit(txt, (10, scr.rct.height - 25))

        pg.display.update()
        tim += 1
        clock.tick(1000)
    
    scr.blit()

    """
    リザルト画面にリザルトを表示
    """

    result = pg.font.Font(None, 400)
    now = time.time()
    txt = result.render(f"loser:{loser}", True, "black") #どちらが負けたかを表示
    scr.sfc.blit(txt, (scr.rct.centerx/2 - 100, scr.rct.centery/2))

    while True:
        scr.blit()
        
        for event in pg.event.get():
            if event.type == pg.QUIT: #リザルト画面を終了
                return
        txt = result.render(f"loser:{loser}", True, "black") #どちらが負けたかを表示
        scr.sfc.blit(txt, (scr.rct.centerx/2 - 100, scr.rct.centery/2))       
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main() # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()