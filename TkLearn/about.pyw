#libraries
from tkinter import *
from tkinter import messagebox
import subprocess
import platform
from tkinter import PhotoImage
#import psutil
from platform import uname
import os
from os import getcwd
#window setup
root=Tk()
ws = root.winfo_screenwidth() 
hs = root.winfo_screenheight() 
w = 1000 
h = 700 
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(True, True)
root.title("Системная информация")
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
        os.system('python3 '+str(getcwd())+'/Main.pyw')
def backesc(placeholder):
    back()
#interface setup
buttonex=Button(root, image=backx32, width=35, compound="left", font=("Consolas", 11),command=back)
buttonex.pack(anchor="nw")
#vars
label=Label(root, text="Билд: v1.2 (стабильный релиз)", font=("Consolas", 15)).pack()
label=Label(root, text="Регулярно проверяйте наличие обновлений на GitHub", font=("Consolas", 15)).pack()
label=Label().pack(pady=20)
txt="Платформа: "+str(platform.system())
label=Label(root, text=txt, font=("Consolas", 12)).pack()
txt="Релиз: "+str(platform.platform())
label=Label(root, text=txt, font=("Consolas", 12)).pack()
txt=f"ОС: {uname().system} {uname().release}, {uname().version}"
label=Label(root, text=txt, font=("Consolas", 12)).pack()
txt="Архитектура (процессор): "+str(platform.machine())+'('+str(platform.processor())+')'
label=Label(root, text=txt, font=("Consolas", 12)).pack()
#txt="ОЗУ: "+str(round(psutil.virtual_memory().total / (1024.0 **3)))+" ГБ"
label=Label().pack(pady=20)
label=Label(root, text="Мы не собираем никакой информации о вашей системе", font=("Consolas", 12)).pack()
label=Label(root, text="Прикрепите скриншот этой страницы если хотите сообщить об ошибке", font=("Consolas", 12)).pack()
label=Label(root, text="Это окно можно масштабировать", font=("Consolas", 12)).pack()
root.bind("<Escape>", backesc)
#over
root.mainloop()
