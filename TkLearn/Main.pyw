# core file of TkLearn
#libraries
import subprocess
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import subprocess
import os
import platform
#vars

#window setup
root=Tk()
root.resizable(False, False)
root.title("TkLearn")
ws = root.winfo_screenwidth() 
hs = root.winfo_screenheight() 
w = 500 
h = 700 
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#root.iconbitmap("appicon-rendered.ico")
cb=(root)
tkx32=PhotoImage(file = r"assets/tkx32.png")
gitx32=PhotoImage(file = r"assets/gitx32.png")
bookx32=PhotoImage(file = r"assets/bookx32.png")
quizx32=PhotoImage(file = r"assets/quizx32.png")
infox32=PhotoImage(file = r"assets/infox32.png")
logox64 = PhotoImage(file = r"assets/tkx64.png")
statsx32 = PhotoImage(file = r"assets/statsx32.png")
logo=Label(root, image=logox64).pack()
#define functions
def Os():
    return platform.system()
if Os()=="Windows":
    root.iconbitmap("appicon-rendered.ico")
def copy():
    messagebox.showinfo("GitHub","https://github.com/average8274")
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
def stats():
    if Os()=="Windows":
        os.startfile("stats.pyw")
        root.destroy()
    else:
        root.destroy()
        os.system("python3 ~/Desktop/TkLearn/TkLearn/stats.pyw")
#interface setup
labels_title=Label(root, text="Добро пожаловать в TkLearn!", font=("Consolas",22))
labels_plain=Label(root)
buttons_githublink=Button(root, text="GitHub",font=("Consolas",10), image=gitx32,compound="left", command=copy)
buttons_about=Button(root, text="О программе", image=infox32, compound="left", font=("Consolas",11),command=about)
buttons_help=Button(root,text="Помощь", font=("Consolas",11),width=18,command=helpwindow)
buttons_dictionary=Button(root,text="Словарь", font=("Consolas",20), image=bookx32, width=400, compound="left", command=dictionary)
buttons_quiz=Button(root,text="Викторина", font=("Consolas",20), image=quizx32, width=400, compound="left",command=quiz)
buttons_stats=Button(root,text="Статистика", font=("Consolas",20), image=statsx32, width=400, compound="left",command=stats)
#wrap up plain interface
labels_title.pack(pady=5)
label=Label(root).pack(pady=5)
buttons_dictionary.pack()
buttons_quiz.pack()
buttons_stats.pack()
label=Label(root).pack(pady=20)
buttons_about.pack()
#buttons_help.pack()
buttons_githublink.pack(pady=100)
#over
root.mainloop()
#no further code will be executed beyond line above
