#libraries
from tkinter import *
from tkinter import messagebox
import subprocess
import platform
import random
import os
from os import getcwd
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
root.title("Вопрос")
backx32=PhotoImage(file = r"assets/backx32.png")
bulbx32=PhotoImage(file = r"assets/bulbx32.png")
submitx32=PhotoImage(file = r"assets/submitx32.png")
nextx32=PhotoImage(file = r"assets/nextx32.png")
crossx32=PhotoImage(file = r"assets/crossx32.png")
tickx32=PhotoImage(file = r"assets/tickx32.png")
arrowx32=PhotoImage(file = r"assets/arrowx32.png")
file=open("cache/window.cache", "w")
file.write("1")
file.close()

def Os():
    return platform.system()
if Os()=="Windows":
    root.iconbitmap("appicon-rendered.ico")
#real functions start here:
file=open("cache/checked.cache","w")
file.write("0")
file.close()
def hint():
    hinttext="Первая буква - "+correct[0]
    messagebox.showinfo("Подсказка",hinttext)
def skip():
    file=open("cache/current.cache", "r")
    current=int(file.readline())
    file.close()
    file=open("cache/.num.cache", "r")
    num=int(file.readline())
    file.close()
    if num==current:
        if Os()=="Windows":
            os.startfile("endquiz.pyw")
            root.destroy()
        else:
            root.destroy()
            os.system('python3 '+str(getcwd())+'/endquiz.pyw')
    else:
        file=open("cache/current.cache", "r")
        current=int(file.readline())
        file.close()
        current+=1
        file=open("cache/current.cache", "w")
        file.write(str(current))
        file.close()
        #print("question self executed")
        if Os()=="Windows":
            os.startfile("question.pyw")
            root.destroy()
        else:
            root.destroy()
            os.system('python3 '+str(getcwd())+'/question.pyw')
def submit():
    file=open("cache/checked.cache","r")
    checked=file.readline()
    file.close()
    if checked=="0":
        answer=((entry.get()).strip())
        if answer==correct:             
            try:
                file=open("telemetry/correct.tele", "r")
                temp=int(file.readline())
                file.close()
                file=open("telemetry/correct.tele", "w")
                temp+=1
                file.write(str(temp))
                file.close()
            except:
                #print("telemetry/correct.tele doesn't exist!")
                file=open("telemetry/correct.tele", "w")
                file.write("1")
            file.close()
            try:
                file=open("cache/correct.cache", "r")
                temp=int(file.readline())
                file.close()
                file=open("cache/correct.cache", "w")
                #print("Correct:",temp+1)
                temp+=1
                file.write(str(temp))
                file.close()
            except:
                #print("cache/correct.cache doesn't exist!")
                file=open("cache/correct.cache", "w")
                file.write("1")
            file.close()
            label=Label(root, image=tickx32, compound="left", fg="green", text="Верно!", font=("Consolas",18)).pack(pady=10)
        else:
            try:
                file = open("dictionaries/mistakes.dic", "r")
            except:
                file = open("dictionaries/mistakes.dic", "w")
            file.close()
            file = open("dictionaries/mistakes.dic", "a+")
            file.write(word+"="+correct+"\n")
            file.close()    
            try:
                file=open("telemetry/n-correct.tele", "r")
                temp=int(file.readline())
                file.close()
                file=open("telemetry/n-correct.tele", "w")
                temp+=1
                file.write(str(temp))
                file.close()
            except:
                #print("telemetry/n-correct.tele doesn't exist!")
                file=open("telemetry/n-correct.tele", "w")
                file.write("1")
            file.close()
            try:
                file=open("cache/n-correct.cache", "r")
                temp=int(file.readline())
                file.close()
                file=open("cache/n-correct.cache", "w")
                #print("Incorrect:",temp+1)
                temp+=1
                file.write(str(temp))
                file.close()
            except:
                #print("cache/n-correct.cache doesn't exist!")
                file=open("cache/n-correct.cache", "w")
                file.write("1")
            file.close()
            label=Label(root, image=crossx32, compound="left", fg="red", text="Неверно!", font=("Consolas",18)).pack(pady=10)
        exitbutton.pack(pady=20)
    checked="1"
    file=open("cache/checked.cache","w")
    file.write(checked)
    file.close()
def exitt():
    file=open("cache/current.cache", "r")
    current=int(file.readline())
    file.close()
    file=open("cache/.num.cache", "r")
    num=int(file.readline())
    file.close()
    if num==current:
        if Os()=="Windows":
            os.startfile("endquiz.pyw")
            root.destroy()
        else:
            root.destroy()
            os.system('python3 '+str(getcwd())+'/endquiz.pyw')
    else:
        file=open("cache/current.cache", "r")
        current=int(file.readline())
        file.close()
        current+=1
        file=open("cache/current.cache", "w")
        file.write(str(current))
        file.close()
        #print("question self executed")
        if Os()=="Windows":
            os.startfile("question.pyw")
            root.destroy()
        else:
            root.destroy()
            os.system('python3 '+str(getcwd())+'/question.pyw')
#vars
elements=[]
file=open("cache/dict.cache", "r")
dict=file.readline()
file.close()
file=open("dictionaries/"+dict+".dic", "r", encoding="utf+8")
for line in file:
    elements.append(line.replace("\n",""))
file=open("cache/current.cache", "r")
current=file.readline()
file.close()
file=open("cache/.num.cache", "r")
num=file.readline()
file.close()
#symbol by symbol looking fo a word
ran=random.randrange(0,len(elements))
element=elements[ran]
char=""
word=""
correct=""
rann=random.randrange(0,1)
if rann==0:
    #print("we are looking at the corresponding (secondary) value")
    char2=''
    a=0
    for char2 in element:
        if char2!="=":
            #print("Looking for an '='...", a, "element '"+char2+"' is not a '=' ")
            a+=1
            if a>100:
                #print("oh fie! looks like program is stuck in an infinite loop looking for a '=' symbol, so it was preventively stopped. You must've been messing with .dic file didnt'u? or...")
                #print("the word is longer than 100 symbols! what kind of language is that?!")
                break
        else:
            #print("gotcha!")
            break
    i=0
    for char in element:
        if i>a:
            correct+=element[i]
        i+=1
    for char in element:
        if char!="=":
            word+=char
        else:
            break
    #print(word)
    #print(word+"="+correct)
else:
    #print("we are looking at the corresponding (secondary) value")
    char2=''
    a=0
    for char2 in element:
        if char2!="=":
            #print("Looking for an '='...", a, "element '"+char2+"' is not a '=' ")
            a+=1
            if a>100:
                #print("oh fie! looks like program is stuck in an infinite loop looking for a '=' symbol, so it was preventively stopped. You must've been messing with .dic file didnt'u? or...")
                #print("the word is longer than 100 symbols! what kind of language is that?!")
                break
        else:
            #print("gotcha!")
            break
    i=0
    for char in element:
        if i>a:
            word+=element[i]
        i+=1
    for char in element:
        if char!="=":
            correct+=char
        else:
            break
    #print(word)
    #print(word+"="+correct)
#wrap up plain interface
txt="Вопрос " + str(current) + " из " + str(num)
label=Label(root, text=txt, font=("Consolas",18)).pack(pady=10)
txt="Введите в поле значение соответствующее "
label=Label(root, text=txt, font=("Consolas",15)).pack(pady=10)
label=Label(root, text=word, font=("Consolas",15)).pack(pady=10)
entry=Entry(root)
entry.pack(pady=20)
submitbutton=Button(root, image=submitx32, width=150, compound="left", text="Подтвердить", command=submit)
submitbutton.pack()
exitbutton=Button(root, image=nextx32, width=150, compound="left", text="Далее", command=exitt)
skipbutton=Button(root, image=arrowx32, width=150, compound="left", text="Пропустить", command=skip)
hintbutton=Button(root, image=bulbx32, width=130, compound="left", text="Подсказка", command=hint)
hintbutton.pack()
skipbutton.pack(pady=15)
#over
root.mainloop()

