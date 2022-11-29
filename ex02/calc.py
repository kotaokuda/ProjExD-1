import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    tkm.showinfo("", f"{num}ボタンがクリックされました")

root = tk.Tk()
root.geometry("300x500")

for i in range(9, -1, -1):
    b = tk.Button(root, text = 9-i, width = 4, height = 2, font = ("", 30))
    b.bind("<1>", button_click)
    b.grid(row = i//3, column = i%3)

root.mainloop()