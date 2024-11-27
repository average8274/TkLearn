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
root.title("Действия со словарями")
backx32=PhotoImage(file = r"assets/backx32.png")
pagex32=PhotoImage(file = r"assets/pagex32.png")
binx32=PhotoImage(file = r"assets/binx32.png")
#vars
############
elements=[]
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
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
listb = Listbox(root, yscrollcommand=scrollbar.set, selectmode=SINGLE)
file=open("dictionaries/.ini.dic", "r", encoding="utf-8")
for line in file:                                               #list all elements in an array
    elements.append(line.replace("\n",""))
    listb.insert(END, line.replace("\n",""))
file.close()
#define functions
def Os():
    return platform.system()
if Os()=="Windows":
    root.iconbitmap("appicon-rendered.ico")
def back():
    if Os()=="Windows":
        os.startfile("dictionary.pyw")
        root.destroy()
    else:
        root.destroy()
        os.system('python3 '+str(getcwd())+'/dictionary.pyw')
def backesc(placeholder):
    back()
def add():
    if entry.get() not in elements:
        file=open("dictionaries/.ini.dic", "a+", encoding="utf-8")
        value=(entry.get()+"\n")
        file.write(value)
        file.close()
        if Os()=="Windows":
            os.startfile("editor.pyw")
            root.destroy()
        else:
            root.destroy()
            os.system('python3 '+str(getcwd())+'/editor.pyw')  
    else:
        messagebox.showerror("Ошибка", "Файл с таким именем уже существует")
def addret(placeholder):
    add()
def remove():
    values=listb.get(ACTIVE)
    path1="dictionaries/.ini.dic"
    f=listb.get(ACTIVE)
    os.remove("dictionaries/"+f+".dic")
    #file=open(path, "r+")
    #values=values+"\n"
    #file.replace(values,"")
    with open(path1, "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open(path1, "w", encoding="utf-8") as f:
        for line in lines:
            if line.strip("\n") != values:
                f.write(line)
    if Os()=="Windows":
        os.startfile("editor.pyw")
        root.destroy()
    else:
        root.destroy()
        os.system('python3 '+str(getcwd())+'/editor.pyw')
#interface setup
buttonex=Button(root, image=backx32, width=35, compound="left", font=("Consolas", 11),command=back)
buttonex.pack(anchor="nw")
label=Label(root,text="Удаление/Добавление словарей",font=("Consolas",14)).pack()
entry=Entry(root)
buttonsub=Button(root, image=pagex32, width=150, compound="left", text="Создать", font=("Consolas", 11),command=add)
buttonrem=Button(root, image=binx32, width=150, compound="left", text="Удалить", font=("Consolas", 11),command=remove)
#wrap up plain interface
listb.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=listb.yview)
entry.pack(pady=20)
buttonsub.pack(pady=10)
buttonrem.pack(pady=10)
root.bind("<Escape>", backesc)
root.bind("<Return>", addret)
#over
root.mainloop()



