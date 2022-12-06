import tkinter as tk
import maze_maker as mm

root = tk.Tk()
root.title("迷えるこうかとん")
Canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
Canvas.pack()
root.mainloop()