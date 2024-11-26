#libraries
from tkinter import *
from tkinter import messagebox
import subprocess
import os
from os import getcwd
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
        os.system('python3 '+str(getcwd())+'/Main.pyw')
#wrap up plain interface
label=Label(root, text="Итог:", font=("Consolas",18)).pack(pady=10)
file=open("cache/correct.cache", "r")
correct=int(file.readline())
file.close()
txt="Верно:"+str(correct)
label=Label(root, image=tickx32, width=250, compound="left", text=txt, font=("Consolas",15), fg="green").pack(pady=10)
file=open("cache/n-correct.cache", "r")
ncorrect=int(file.readline())
file.close()
txt="Неверно:"+str(ncorrect)
label=Label(root, image=crossx32, width=250, compound="left", text=txt, font=("Consolas",15), fg="red").pack(pady=10)
file=open("cache/current.cache", "r") 
total=int(file.readline())
txt="Пропущено:"+str(total-ncorrect-correct)
label=Label(root, image=arrowx32, width=250, compound="left", text=txt, font=("Consolas",15), fg="grey").pack(pady=10)
button=Button(root, text="Выход", font=("Consolas",15), command=back)
button.pack(pady=20)
#over
root.mainloop()