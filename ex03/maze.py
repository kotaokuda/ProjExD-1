import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm
import time

def main_proc():
    global cx, cy, key, mx, my, R, image
    if (key == "Up"):
        l1 = maze[mx][my-1]
        if(check_mxy(l1)): #mx、myが要件を満たしているかチェックするための関数を呼び出す#42
            my -= 1
    if (key == "Down"):
        l2 = maze[mx][my+1]
        if(check_mxy(l2)):
            my += 1
    if (key == "Left"):
        l3 = maze[mx-1][my]
        if(check_mxy(l3)):
            mx -= 1
    if (key == "Right"):
        l4 = maze[mx+1][my]
        if(check_mxy(l4)):
            mx += 1
    if(maze[mx][my] == "R"):
        R = True
    mx, my = check_xy(mx, my)
    cx = 50 + mx * 100
    cy = 50 + my * 100
    Canvas.coords("Kouka", cx, cy)
    if(key == "Left"): #左を向いたときに画像を変更
        image = tk.PhotoImage(file="fig/5.png")
        Canvas.itemconfig("Kouka", image=image)
    if(key == "Right"): #右を向いたときに画像を変更
        image = tk.PhotoImage(file="fig/2.png")
        Canvas.itemconfig("Kouka", image=image)
    if(maze[mx][my] == "G"): #ゴールに着いたときに画像を変更
        image = tk.PhotoImage(file="fig/6.png")
        image1 = image.zoom(5,5) #画像を5倍に拡大
        Canvas.itemconfig("Kouka", image=image1)
        goal_message()

def check_mxy(rule): #maze[mx][my]が進行可能なマスか調べる関数
    if(R):
        rl = rule == 1 or rule == "G" or rule == "R" 
    else:
        rl = rule == 0 or rule == "S" or rule == "R"        
    return rl

def check_xy(mx, my): #mx,myがlist範囲を出ないかチェックする関数
    if (0 > mx):
        mx = 0
    elif (15 <= mx):
        mx = 14
    if (0 > my):
        my = 0
    elif (9 <= my):
        my = 8
    return mx, my

def key_up(event):
    global key
    key = ""

def key_down(event):
    global key
    key = event.keysym
    root.after(50,main_proc)

def maze_update(): #迷路のマスの色などを書き換える関数
    global cx, cy
    finst = False
    fingo = False
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (maze[i][j] == 0):
                maze[i][j] = "S"
                Canvas.create_rectangle(i*100, j*100, i*100+100, j*100+100, fill="yellow")
                cx = i*100 + 50
                cy = j*100 + 50
                finst = True
                break
        if(finst):
            break
    for n in range(1, len(maze) - 2):
        for k in range(1, len(maze[0]) - 2):
            if(maze[n][k] == 1):
                maze[n][k] = "G"
                Canvas.create_rectangle(n*100, k*100, n*100+100, k*100+100, fill="pink")
                fingo = True
                break
        if(fingo):
            break
    maze[-2][-1] = "R"
    Canvas.create_rectangle(1300, 800, 1400, 900, fill="orange")

def goal_message():
    endtime = time.time()
    goal = endtime - starttime
    ask = tkm.askquestion("Clear", f"あなたのクリアタイムは{int(goal)}秒です。\tもう一度プレイしますか(未完成機能)")
    # if(ask =="yes"):
    #     root.destroy
    #     InitAndPlayMaze()
    # else:
    #     root.destroy

def InitAndPlayMaze(): # 関数にしたらToDoの迷路を作り直す機能が作りやすいかなと考え追加したが、間に合わず無用の長物と化した関数
    global cx, cy, mx, my, key, R, G, starttime, maze, Canvas, root, image
    cx, cy = 150, 150
    mx, my = 1, 1
    key = ""
    R = False # 壁に上るマスを通過したかどうかの判定
    G = False # ゴールしたかどうかの判定
    starttime = time.time() #クリア時間の計測、スタート時間
    root = tk.Tk()
    root.title("迷えるこうかとん")
    Canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    maze = mm.make_maze(15,9)
    mm.show_maze(Canvas, maze)
    maze_update() # maze.pyの変更だけで完結させるつもりで作ったので、ゴールマスの色塗り替えなどを行うための関数
    image = tk.PhotoImage(file="fig/8.png")
    Canvas.create_image(cx, cy, image=image, tag="Kouka")
    Canvas.pack()
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.mainloop()

if __name__ == "__main__":
    InitAndPlayMaze() #関数にしたらToDoの迷路を作り直す機能が作りやすいかなと考え関数にまとめたが、間に合わなかったので無意味に使用される関数#106