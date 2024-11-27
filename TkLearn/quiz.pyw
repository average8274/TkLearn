#libraries
from tkinter import *
from tkinter import messagebox
import subprocess
import os
from os import getcwd
import platform
#script handler, no interface

#vars
#define
def Os():
    return platform.system()
elements=[]
file=open("cache/dict.cache", "r")
dict=file.readline()
file.close()
file=open("dictionaries/"+dict+".dic", "r")
for line in file:
    elements.append(line.replace("\n",""))
file=open("cache/.num.cache", "r")
num=int(file.readline())
file.close()
current=1
mistakes=0
correct=0
file=open("cache/correct.cache", "w")
file.write("0")
file.close()
file=open("cache/n-correct.cache", "w")
file.write("0")
file.close()
file=open("cache/current.cache", "w")
file.write("1")
file.close()
#print("successfully identified the quiz")
if Os()=="Windows":
    os.startfile("question.pyw")
else:
    os.system('python3 '+str(getcwd())+'/question.pyw')
#window="0"
#file=open("cache/window.cache", "w")
#file.write(window)
#file.close()
#os.startfile("question.pyw")
#while current<=num:
#    file=open("cache/window.cache", "r")
#    window=file.readline()
#    file.close()
#    while window=="0":
#        file=open("cache/current.cache", "w")   #I HAVE NO IDEA WHY IT WORKS, JUST DON'T TOUCH IT!
#        file.write(str(current))                #HECK! IT ONLY WORKS ON LINUX!
#        file.close()                            #To be revised. Saved as a working piece of code to be reused, and as a tribute to my ingenuity
#        if window=="0":                         
#            if Os()=="Windows":
#                print("quiz launches a window")
#                #os.startfile("question.pyw")
#                current+=1
#            else:
#                os.system("python3 ~/Desktop/TkLearn/TkLearn/question.pyw")
#            file=open("cache/window.cache", "w")
#            file.write("1")
#            file.close()
#        file=open("cache/window.cache", "r")
#        window=file.readline()
#        file.close()
#    file=open("cache/current.cache", "r")
#    current=int(file.readline())
#    file.close()
#    file=open("cache/.num.cache", "r")
#    num=int(file.readline())
#    file.close()
#    if num<current:
#        break
#messagebox.showinfo("Внимание", "Блиц-опрос завершен")
#if Os()=="Windows":
#    os.startfile("endquiz.py")
#else:
#    os.system("python3 ~/Desktop/TkLearn/TkLearn/endquiz.pyw")