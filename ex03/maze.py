import tkinter as tk
import maze_maker as mm

def key_up(event):
    global key
    key = ""

def key_down(event):
    global key
    key = event.keysym

if __name__ == "__main__":
    cx = 300
    cy = 400
    key = ""
    root = tk.Tk()
    root.title("迷えるこうかとん")
    Canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    image = tk.PhotoImage(file="fig/0.png")
    Canvas.create_image(cx, cy, image=image)
    Canvas.pack()
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.mainloop()