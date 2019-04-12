from tkinter import *
root = Tk()
root.geometry("733x566")
root.title("Pycharm")

def myfunc():
    print("Mai ek bahut hi natkhat aur shaitaan function hoon")
def myfunc1():
    print("project started")
def myfunc2():
    print("file saved")
def myfunc3():
    print("file saved as ")
def myfunc4():
    print("printed")
def myfunc5():
    print("cutted")
def myfunc6():
    print("copied")

def myfunc7():
    print("pasted")

def myfunc8():
    print("finded")

# #Use these to create a non dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)


mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New project", command=myfunc1)
m1.add_command(label="Save", command=myfunc2)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc3)
m1.add_command(label="Print", command=myfunc4)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc5)
m2.add_command(label="Copy", command=myfunc6)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc7)
m2.add_command(label="Find", command=myfunc8)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

root.mainloop()
