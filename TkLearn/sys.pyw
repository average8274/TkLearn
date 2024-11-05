from tkinter import *
import os
import platform
from tkinter import PhotoImage
root=Tk()
root.title("О программе")
ws = root.winfo_screenwidth() 
hs = root.winfo_screenheight() 
w = 500 
h = 700 
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(False,False)
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
def sys():
    if Os()=="Windows":
        os.startfile("sys.pyw")
        root.destroy()
    else:
        root.destroy()
        os.system("python3 ~/Desktop/TkLearn/TkLearn/sys.pyw")
backx32=PhotoImage(file = r"assets/backx32.png")
buttonex=Button(root, image=backx32, width=35, compound="left", font=("Consolas", 11),command=back)
buttonex.pack(anchor="nw")
label=Label(root, text="Информация о программе:", font=("Consolas", 15)).pack(pady=10)
label=Label(root, text="Билд: public01", font=("Consolas", 15)).pack()
label=Label(root, text="Создано с помощью Tkinter", font=("Consolas", 15)).pack()
buttons_sys=Button(root,text="Системная информация", font=("Consolas",12),command=sys)
buttons_sys.pack(pady=20)
root.mainloop()
