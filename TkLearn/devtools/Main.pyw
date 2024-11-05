# core file of TkLearn
#libraries
import subprocess
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import subprocess
import os
import pyperclip
import platform
#vars

#window setup
root=Tk()
root.geometry("500x700")
root.resizable(False, False)
root.title("TkLearn")
#root.iconbitmap("appicon-rendered.ico")
cb=(root)
tkx32=PhotoImage(file = r"assets/tkx32.png")
gitx32=PhotoImage(file = r"assets/gitx32.png")
bookx32=PhotoImage(file = r"assets/bookx32.png")
quizx32=PhotoImage(file = r"assets/quizx32.png")

#define functions
def Os():
    return platform.system()
if Os()=="Windows":
    root.iconbitmap("appicon-rendered.ico")
def copy():
    if Os()=="Windows":
        messagebox.showinfo("Внимание","Ссылка на GitHub скопирована в буфер обмена")
        txt="https://github.com/CatPlayer0"
        cmd='echo '+txt.strip()+'|clip'
        return subprocess.check_call(cmd, shell=True)
    else:
        messagebox.showinfo("Внимание","Ссылка на GitHub скопирована в буфер обмена")
        pyperclip.copy("https://github.com/CatPlayer0")
def helpwindow():
    if Os()=="Windows":
        os.startfile("help.pyw")
        root.destroy()
    else:
        root.destroy()
        os.system("python3 ~/Desktop/TkLearn/TkLearn/help.pyw")
def about():
    if Os()=="Windows":
        os.startfile("about.pyw")
        root.destroy()
    else:
        root.destroy()
        os.system("python3 ~/Desktop/TkLearn/TkLearn/about.pyw")
def dictionary():
    if Os()=="Windows":
        os.startfile("dictionary.pyw")
        root.destroy()
    else:
        root.destroy()
        os.system("python3 ~/Desktop/TkLearn/TkLearn/dictionary.pyw")
def quiz():
    if Os()=="Windows":
        os.startfile("quizselect.pyw")
        root.destroy()
    else:
        root.destroy()
        os.system("python3 ~/Desktop/TkLearn/TkLearn/quizselect.pyw")
#interface setup
labels_title=Label(root, text="Добро пожаловать в TkLearn!", font=("Consolas",22))
labels_plain=Label(root)
buttons_githublink=Button(root, text="GitHub",font=("Consolas",10), image=gitx32,compound="left", command=copy)
buttons_about=Button(root, text="О программе", image=tkx32, compound="left", font=("Consolas",11),command=about)
buttons_help=Button(root,text="Помощь", font=("Consolas",11),width=18,command=helpwindow)
buttons_dictionary=Button(root,text="Словарь", font=("Consolas",20), image=bookx32, width=400, compound="left", command=dictionary)
buttons_quiz=Button(root,text="Викторина", font=("Consolas",20), image=quizx32, width=400, compound="left",command=quiz)
#wrap up plain interface
labels_title.pack(pady=20)
buttons_dictionary.pack()
buttons_quiz.pack()
label=Label(root).pack(pady=20)
buttons_about.pack()
#buttons_help.pack()
buttons_githublink.pack(pady=100)
#over
root.mainloop()
#no further code will be executed beyond line above
