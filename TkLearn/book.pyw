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
root.resizable(True, False)
root.title("Просмотр/Редактирование содержимого")
#vars
backx32=PhotoImage(file = r"assets/backx32.png")
pencilx32=PhotoImage(file = r"assets/pencilx32.png")
eraserx32=PhotoImage(file = r"assets/eraserx32.png")
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
    a = "=" in entry1.get()
    b = "=" in entry2.get()
    value1=(entry1.get()).strip()
    value2=(entry2.get()).strip()
    if a == False and b == False:
        file=open("dictionaries/"+dict+".dic", "a+", encoding="utf-8")
        value=(value1+"="+value2+"\n")
        file.write(value)
        file.close()
        if Os()=="Windows":
            os.startfile("book.pyw")
            root.destroy()
        else:
            root.destroy()
            os.system('python3 '+str(getcwd())+'/book.pyw')
    else:
        messagebox.showerror("Ошибка", "Значение не может содержать символ '=' ")
def addret(placeholder):
    add()
def remove():
    values=listb.get(ACTIVE)
    path="dictionaries/"+dict+".dic"
    #file=open(path, "r+")
    #values=values+"\n"
    #file.replace(values,"")
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            if line.strip("\n") != values:
                f.write(line)
    if Os()=="Windows":
        os.startfile("book.pyw")
        root.destroy()
    else:
        root.destroy()
        os.system('python3 '+str(getcwd())+'/book.pyw')
#interface setup
entry1=Entry(root, width=15)
entry2=Entry(root, width=15)
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
listb = Listbox(root, yscrollcommand=scrollbar.set, selectmode=SINGLE, width=0)
buttonex=Button(root, image=backx32, width=35, compound="left", font=("Consolas", 11),command=back)
buttonsub=Button(root, image=pencilx32, width=90, compound="left", text="Внести", font=("Consolas", 11), command=add)
buttonrem=Button(root, image=eraserx32, width=90, compound="left", text="Удалить", font=("Consolas", 11),command=remove)
#grab .DIC file
file=open("cache/dict.cache", "r", encoding="utf-8")
dict=file.readline()
file.close()
file=open("dictionaries/"+dict+".dic", "r", encoding="utf-8")
n=0
listtt=[]
for line in file:
    isInList=line.replace("\n","") in listtt
    n+=1
    if isInList==False:
        listb.insert(END, line.replace("\n",""))
        listtt.append(line.replace("\n",""))
if n==0:
    listb.insert(END, "--Словарь пуст--")
#for line in file:
#    listb.insert(END, line.replace("\n",""))
file.close()
dicti=dict
txt="Редактирование",dicti
buttonex.pack(anchor="nw")
label=Label(root,text=txt,font=("Consolas",14)).pack()
#wrap up plain interface
label=Label(root,text="=",font=("Consolas",14))
listb.pack(side=RIGHT, fill=BOTH)
scrollbar.config(command=listb.yview)
entry1.place(x=10,y=100)
label.place(x=140, y=100)
entry2.place(x=160,y=100)
buttonsub.place(x=90,y=130)
buttonrem.place(x=90,y=270)
root.bind("<Return>", addret)
root.bind("<Escape>", backesc)
#over
root.mainloop()



