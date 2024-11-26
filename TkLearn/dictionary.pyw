#libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import subprocess
import os
from os import getcwd
import platform
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
root.title("Словарь")
backx32=PhotoImage(file = r"assets/backx32.png")
submitx32=PhotoImage(file = r"assets/submitx32.png")
booksx32=PhotoImage(file = r"assets/booksx32.png")
#vars
file=0
elements=[]
#define functions
def Os():
    return platform.system()
if Os()=="Windows":
    root.iconbitmap("appicon-rendered.ico")
def submission():
    choice = cb.get()
    if choice in elements:
        file=open("cache/dict.cache", "w", encoding="utf-8", )
        file.write(choice)
        file.close()
        if Os()=="Windows":
            os.startfile("book.pyw")
            root.destroy()
        else:
            root.destroy()
            os.system('python3 '+str(getcwd())+'/book.pyw')
    else:
        messagebox.showerror("Ошибка", "Введено недействительное значение")
def back():
    if Os()=="Windows":
        os.startfile("Main.pyw")
        root.destroy()
    else:
        root.destroy()
        os.system('python3 '+str(getcwd())+'/Main.pyw')
def bookeditor():
    if Os()=="Windows":
        os.startfile("editor.pyw")
        root.destroy()
    else:
        root.destroy()
        os.system('python3 '+str(getcwd())+'/editor.pyw')
#interface setup
submit=Button(root, image=submitx32, width=150, compound="left", text="Подтвердить", font=("Consolas", 13), command=submission)
edit=Button(root, image=booksx32, width=150, compound="left", text="Управлять", font=("Consolas", 13), command=bookeditor)
#initializing local dictionaries
try:
    file=open("dictionaries/.ini.dic", "r", encoding="utf-8")
    file.close()
except:
    file=open("dictionaries/.ini.dic", "w", encoding="utf-8")
    file.close()
#########
file=open("dictionaries/.ini.dic", "r", encoding="utf-8")
for line in file:                                               #list all elements in an array
    elements.append(line.replace("\n",""))
for i in range(len(elements)):
    path="dictionaries/"+elements[i]+".dic"
    try:
        file=open(path, "r", encoding="utf-8")
        file.close()
    except:
        #print("file doesn't exist")
        file=open(path, "w", encoding="utf-8")
        file.close()
#wrap up plain interface
buttonex=Button(root, image=backx32, width=35, compound="left", font=("Consolas", 11),command=back)
buttonex.pack(anchor="nw")
cb=ttk.Combobox(root, values = elements)
label=Label(root, text="Выберите словарь", font=("Consolas", 15)).pack(pady=10)
cb.pack()
submit.pack(pady=20)
edit.pack(pady=50)

#over
root.mainloop()
