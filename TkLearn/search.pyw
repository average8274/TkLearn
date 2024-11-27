#libraries
from tkinter import *
from tkinter import messagebox
import platform
from tkinter import PhotoImage
from tkinter import ttk
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
root.title("Поиск")
backx32=PhotoImage(file = r"assets/backx32.png")
magx32=PhotoImage(file = r"assets/magx32.png")
#define functions
def Os():
    return platform.system()
if Os()=="Windows":
    root.iconbitmap("appicon-rendered.ico")
def backesc(placeholder):
    back()
def back():
    cache=open("cache/results.cache", "w", encoding="utf-8")
    cache.write("")
    cache.close()
    if Os()=="Windows":
        os.startfile("dictionary.pyw")
        root.destroy()
    else:
        root.destroy()
        os.system('python3 '+str(getcwd())+'/dictionary.pyw')
def searchret(placeholder):
    search()
def search():
    try:
        cache=open("cache/results.cache", "r")
        cache.close()
    except:
        cache=open("cache/results.cache", "w")
        cache.close()
    cache=open("cache/results.cache", "w")
    cache.write("")
    item=entry.get()
    #print("searching for", item)
    init=open("dictionaries/.ini.dic", "r", encoding="utf-8")
    for line1 in init:
        #print("Looking into ", line1)
        file=open("dictionaries/"+line1.replace("\n","")+".dic", "r", encoding="utf-8")
        for line2 in file:
            #print("checking if ", item, "is in", line2)
            contain=item.strip().lower() in line2.replace("\n","").strip().lower()
            #print(contain)
            if contain == True:
                #print("now writing...")
                cache=open("cache/results.cache", "a+", encoding="utf-8")
                cache.write(line2)
                cache.close()
    if Os()=="Windows":
        os.startfile("search.pyw")
        root.destroy()
    else:
        root.destroy()
        os.system('python3 '+str(getcwd())+'/search.pyw')
    init.close()
    file.close()
#interface setup
entry=Entry(root)
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
listb = Listbox(root, yscrollcommand=scrollbar.set, selectmode=SINGLE)
buttonex=Button(root, image=backx32, width=35, compound="left", font=("Consolas", 11),command=back)
submitbutton=Button(root, image=magx32, width=150, compound="left", text="Искать", font=("Consolas", 13), command=search)
#vars

#wrap up plain interface
try:
    cache=open("cache/results.cache", "r")
    cache.close()
except:
    cache=open("cache/results.cache", "w")
    cache.close()
file=open("cache/dict.cache", "r")
dict=file.readline()
file.close()
file=open("cache/results.cache", "r", encoding="utf-8")
listtt=[]
n=0
for line in file:
    isInList=line.replace("\n","") in listtt
    n+=1
    if isInList==False:
        listb.insert(END, line.replace("\n",""))
        listtt.append(line.replace("\n",""))
if n==0:
    listb.insert(END, "--Ничего не найдено--")
file.close()
#wrap up plain interface
buttonex.pack(anchor="nw")
label=Label(root, text="Поиск по словарям", font=("Consolas", 15)).pack(pady=10)
listb.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=listb.yview)
entry.pack(pady=10)
submitbutton.pack(pady=5)
root.bind("<Escape>", backesc)
root.bind("<Return>", searchret)
#over
root.mainloop()