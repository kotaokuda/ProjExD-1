import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.geometry("300x500")

for i in range(9, -1, -1):
    b = tk.Button(root, text = 9-i, width = 4, height = 2, font = ("", 30))
    b.grid(row = i//3, column = i%3)

root.mainloop()