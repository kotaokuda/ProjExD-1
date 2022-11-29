import tkinter as tk

def button_click(event,str = "None"):
    global mark
    btn = event.widget
    if(str=="None"):
        num = btn["text"]
    else:
        num = str
    if(mark):
        entry.insert(tk.END, num)
    else:
        if(num in ng):
            mark = False
        else:
            mark = True
            entry.insert(tk.END, num)
    if(num in ng):
        mark = False

def calc_num(event):
    calc = entry.get()
    for i, eo in enumerate(evaloperation):
        calc = calc.replace(operations[i],eo)
    calc = calc.replace("^","**")
    calc = calc.replace("√","**(1/2)")
    calc = calc + ")"*kaca
    result = eval(calc)
    entry.delete(0,tk.END)
    entry.insert(tk.END, result)

def delate_num(event):
    den = entry.get()
    entry.delete(len(den) - 1)

def c_delate(event):
    entry.delete(0,tk.END)

def percent(event):
    per = entry.get()
    eper = eval(per)
    entry.delete(0,tk.END)
    entry.insert(tk.END, eper/100)

def tx(event):
    txen = entry.get()
    if(len(txen)>0):
        tlist = list(txen)
        if(tlist[-1] in ng):
            return
        else:
            tt = txen 
            for op in operations:
                 tt= tt.replace(op," ")
            tt = tt.split(" ")
            entry.delete(len(txen)-len(tt[-1]),tk.END)
            entry.insert(tk.END,1/int(tt[-1]))

def kako(event):
    global kaca
    entry.insert(tk.END, "(")
    kaca += 1

def kakotoji(event):
    global kaca
    entry.insert(tk.END, ")")
    kaca -= 1

def x2(event):
    button_click(event, "^")

def rootx(event):
    button_click(event, "√")

root = tk.Tk()
root.geometry("300x500")


f = 20
w = 4
h = 1
mark = False
kaca = 0

entry = tk.Entry(root, justify = "right", width = 10, font = ("", 40))
entry.grid(row = 0, column = 0, columnspan = 4)

command = ["%", "1/x","C", "[X]", "x^2", "√x", "(", ")"]
binds = [percent, tx, c_delate, delate_num, x2, rootx, kako,kakotoji]
for j,c in enumerate(command):
    bc = tk.Button(root, text = c, width = w, height = h, font = ("", f))
    bc.bind("<1>", binds[j])
    bc.grid(row = 1+j//4, column = j%4)

for i in range(9, -1, -1):
    b = tk.Button(root, text = 9-i, width = w, height = h, font = ("", f))
    b.bind("<1>", button_click)
    if(i != 9):
        b.grid(row = 3+i//3, column = 2-i%3)
        continue
    b.grid(row = 6, column = 0)

dot = tk.Button(root, text = ".", width = w, height = h, font = ("", f))
dot.bind("<1>", button_click)
dot.grid(row = 6, column = 1)

operations = ["÷", "×", "-", "+"]
evaloperation = ["/", "*"]

for i, o in enumerate(operations):
    bo = tk.Button(root, text = o, width = w, height = h, font = ("", f)) 
    bo.bind("<1>", button_click)
    bo.grid(row = 3+i, column = 3 )

buttonE = tk.Button(root, text = "=", width = w, height = h, font = ("", f))
buttonE.bind("<1>", calc_num)
buttonE.grid(row = 6, column = 2)

ng = operations+[".","^"]

root.mainloop()