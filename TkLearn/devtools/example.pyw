#libraries
from tkinter import *
from tkinter import messagebox
import subprocess
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
root.title("Example")
backx32=PhotoImage(file = r"assets/backx32.png")
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
#interface setup
buttonex=Button(root, image=backx32, width=35, compound="left", font=("Consolas", 11),command=back)
#vars

#wrap up plain interface
buttonex.pack(anchor="nw")
#over
root.mainloop()