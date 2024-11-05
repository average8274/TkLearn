#f=open("dictionaries/.ini.dic")
#for line in f:
#    if line==" ":
#        f.writelines("")
a=input("Wordbook for fixing => ")
file=open("dicionaries/",a)
counter=0
total=0
for line in file:
    total+=1
line=""
while counter<=total:
    
    for line in file:
        if line == "\n":
            for 
