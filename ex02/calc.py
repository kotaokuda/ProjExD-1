import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    tkm.showinfo("", f"{num}ボタンがクリックされました")

root = tk.Tk()
root.geometry("300x500")

enrty = tk.Entry(root, justify = "right", width = 10, font = ("", 40))
enrty.grid(row = 0, column = 0, columnspan = 3)

for i in range(9, -1, -1):
    b = tk.Button(root, text = 9-i, width = 4, height = 2, font = ("", 30))
    b.bind("<1>", button_click)
    b.grid(row = 1+i//3, column = i%3)

buttonP = tk.Button(root, text = "+", width = 4, height = 2, font = ("", 30))
buttonP.grid(row = 4, column = 1 )
buttonE = tk.Button(root, text = "=", width = 4, height = 2, font = ("", 30))
buttonE.grid(row = 4, column = 2)

root.mainloop()