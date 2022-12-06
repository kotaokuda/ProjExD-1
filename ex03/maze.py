import tkinter as tk
import maze_maker as mm

def main_proc():
    global cx, cy, key, mx, my
    if (key == "Up"):
        if(maze[mx][my-1] == 0):
            my -= 1
    if (key == "Down"):
        if(maze[mx][my+1] == 0):
            my += 1
    if (key == "Left"):
        if(maze[mx-1][my] == 0):
            mx -= 1
    if (key == "Right"):
        if(maze[mx+1][my] == 0):
            mx += 1
    cx = 50 + mx * 100
    cy = 50 + my * 100
    Canvas.coords("Kouka", cx, cy)

def key_up(event):
    global key
    key = ""

def key_down(event):
    global key
    key = event.keysym
    root.after(10,main_proc)

if __name__ == "__main__":
    cx = 150
    cy = 150
    mx = 1
    my = 1
    key = ""
    root = tk.Tk()
    root.title("迷えるこうかとん")
    Canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    maze = mm.make_maze(15,9)
    mm.show_maze(Canvas, maze)
    image = tk.PhotoImage(file="fig/0.png")
    Canvas.create_image(cx, cy, image=image, tag="Kouka")
    Canvas.pack()
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.mainloop()