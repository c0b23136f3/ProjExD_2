import os
import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900
DELTA = {  # 移動量辞書（押下キー：移動量タプル）
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
}
def kadai3():
 """課題３
 は
 失敗しました
 """
 screen = pg.display.set_mode((800, 600))     #課題３の失敗作
 sikaku=pg.Surface((20,20))
 pg.draw.rect(sikaku,(255,255,255),(10,10),10)
 fonto = pg.font.Font(None, 80)
 txt = fonto.render("hello", True, (0, 0, 0))
 screen.blit(sikaku, [300, 200])
 pg.display.update()

 screen=pg.display.set_mode((800,600))
 enn=pg.Surface((20,20))
 pg.draw.circle(enn,(255,0,0),(10,10),10)
 screen.blit()

 fonto = pg.font.Font(None, 80) 
 txt = fonto.render("hello", True, (255, 255, 255)) 
 screen.blit(txt, [300, 200])                #ここまで
print(kadai3.__doc__)

os.chdir(os.path.dirname(os.path.abspath(__file__)))
def check_bound(obj_rct:pg.Rect) -> tuple[bool, bool]:
   
    yoko, tate = True, True
    if obj_rct.left < 0 or WIDTH < obj_rct.right: 
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        tate = False
    return yoko, tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    # ここからこうかとんの設定
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400

    KOUKATONMUKI={
    pg.K_UP: pg.transform.rotozoom(kk_img, 280, 1.0),     #課題１の辞書
    pg.K_DOWN: pg.transform.rotozoom(kk_img, 90, 1.0),
    pg.K_LEFT: pg.transform.rotozoom(kk_img, 0, 1.0),
    pg.K_RIGHT: pg.transform.rotozoom(kk_img, 180, 1.0),
}

    # ここから爆弾の設定
    bd_img = pg.Surface((20, 20))
    bd_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)
    bd_rct = bd_img.get_rect()
    bd_rct.center = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    vx, vy = +5, +5  

    accs = [a for a in range(1, 11)]      #課題２の途中
    for r in range(1, 11):
        bb_img = pg.Surface((20*r, 20*r)) 
        pg.draw.circle(bb_img, (255, 0, 0), (10*r, 10*r), 10*r)
        bb_accs:int=0
        bb_imgs;int=0
        tmr=1
        avx = vx*bb_accs[min(tmr//500, 9)] 
        bb_img = bb_imgs[min(tmr//500, 9)]

    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        if kk_rct.colliderect(bd_rct): #こうかトンと爆弾がぶつかったら
            
            print("Game Over")
            return
        screen.blit(bg_img, [0, 0]) 

        # こうかとんの移動と表示
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, v in DELTA.items():
            if key_lst[k]:
               sum_mv[0] += v[0]
               sum_mv[1] += v[1]

        for l,r in KOUKATONMUKI.items():    #課題３の失敗作
            if key_lst[l]:
                kk_img[0]+=r[0]
                kk_img[1]+=r[1]
        
        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(kk_img, kk_rct)
        bd_rct.move_ip(vx, vy)       
        screen.blit(bd_img, bd_rct)
        yoko, tate = check_bound(bd_rct)
        if not yoko: 
            vx *= -1
        if not tate:  
            vy *= -1
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
