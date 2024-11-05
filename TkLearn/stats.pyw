#libraries
from tkinter import *
from tkinter import messagebox
import subprocess
import os
import platform
from tkinter import PhotoImage
#window setup
root=Tk()
ws = root.winfo_screenwidth() 
hs = root.winfo_screenheight() 
w = 500 
h = 700 
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(False, False)
root.title("Итоги")
backx32=PhotoImage(file = r"assets/backx32.png")
submitx32=PhotoImage(file = r"assets/submitx32.png")
nextx32=PhotoImage(file = r"assets/nextx32.png")
crossx32=PhotoImage(file = r"assets/crossx32.png")
tickx32=PhotoImage(file = r"assets/tickx32.png")
arrowx32=PhotoImage(file = r"assets/arrowx32.png")
eraserx32=PhotoImage(file = r"assets/eraserx32.png")
#define functions
def Os():
    return platform.system()
if Os()=="Windows":
    root.iconbitmap("appicon-rendered.ico")
def back():
    if Os()=="Windows":
        os.startfile("Main.pyw")
        root.destroy()
    else:
        root.destroy()
        os.system("python3 ~/Desktop/TkLearn/TkLearn/Main.pyw")
def remove():
    file=open("telemetry/correct.tele", "w")
    file.write("0")
    file.close()
    file=open("telemetry/n-correct.tele", "w")
    file.write("0")
    file.close()
    if Os()=="Windows":
        os.startfile("stats.pyw")
        root.destroy()
    else:
        root.destroy()
        os.system("python3 ~/Desktop/TkLearn/TkLearn/stats.pyw")
#wrap up plain interface
buttonex=Button(root, image=backx32, width=35, compound="left", font=("Consolas", 11),command=back)
buttonex.pack(anchor="nw")
label=Label(root, text="Статистика:", font=("Consolas",18)).pack(pady=10)
file=open("telemetry/correct.tele", "r")
correct=int(file.readline())
file.close()
txt="Верно:"+str(correct)
label=Label(root, image=tickx32, width=200, compound="left", text=txt, font=("Consolas",15), fg="green").pack(pady=10)
file=open("telemetry/n-correct.tele", "r")
ncorrect=int(file.readline())
file.close()
txt="Неверно:"+str(ncorrect)
label=Label(root, image=crossx32, width=200, compound="left", text=txt, font=("Consolas",15), fg="red").pack(pady=10)
buttonrem=Button(root, image=eraserx32, width=90, compound="left", text="Удалить", font=("Consolas", 11),command=remove)
buttonrem.pack(pady=10)
#over
root.mainloop()