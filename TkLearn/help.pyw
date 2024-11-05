from tkinter import *
import os
import platform
root=Tk()
root.title("Помощь")
ws = root.winfo_screenwidth() 
hs = root.winfo_screenheight() 
w = 500 
h = 700 
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(False,False)
#help.iconbitmap("appicon-rendered.ico")
label=Label(root, text="TkLearn это программа, которая признана помочь в запоминании", font=("Consolas", 15)).pack(pady=10)
label=Label(root, text="разных вещей, будь то слова из иностранного языка, формулы,", font=("Consolas", 15)).pack()
label=Label(root, text="или что-то еще. Словари - это файлы, содержащие набор слов и", font=("Consolas", 15)).pack()
label=Label(root, text="соответствующие им значения, например: слово на английском и ", font=("Consolas", 15)).pack()
label=Label(root, text="его перевод. Словари можно просматривать, а также тренировать", font=("Consolas", 15)).pack()
label=Label(root, text="в разделе 'тренировка'", font=("Consolas", 15)).pack()
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
        os.system('python3 ~/Desktop/TkLearn/TkLearn/Main.pyw')
button=Button(root, text="Назад", font=("Consolas", 11),command=back)
button.pack(pady=10)
root.mainloop()
