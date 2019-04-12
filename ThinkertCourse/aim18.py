from tkinter import *
root = Tk()
root.geometry("455x233")
root.title("scroll bar")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root,yscrollcommand=scrollbar.set)
for i in range(344):
    listbox.insert(END, f"Item{i}")
# listbox.pack(fill="both", padx=22)
text = Text(root, yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command=listbox.yview)



from tkinter import *
import tkinter.messagebox as tmsg

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
def help():
    print("I will help you")
    a = tmsg.showinfo("help","vishal will help you")
def rate():
    print("how much u want rate us")
    value=tmsg.askquestion("was ur experience good ","You used this gui... was you")
    print(value)
    if value == "yes":
        msg="Great. Rate us on "
    else:
        msg="Tell us what went wrong. we will call you soon"
    tmsg.showinfo("Experiance",msg)
def divya():
    ans = tmsg.askretrycancel("Divya se dosti karlo", "Sorry divya nahi banegi appki dost")
    if ans:
        print("retry karne pe bhi kuch nahi hoga")
    else:
        print("bahut badiyaa bhai cancel kar diya warna pitte")

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


m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Cut", command=myfunc5)
m3.add_command(label="Copy", command=myfunc6)
m3.add_separator()
m3.add_command(label="Paste", command=myfunc7)
m3.add_command(label="Find", command=myfunc8)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="View", menu=m3)

m4 = Menu(mainmenu, tearoff=0)
m4.add_command(label="Cut", command=myfunc5)
m4.add_command(label="Copy", command=myfunc6)
m4.add_separator()
m4.add_command(label="Paste", command=myfunc7)
m4.add_command(label="Find", command=myfunc8)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Navigate", menu=m4)

m5 = Menu(mainmenu, tearoff=0)
m5.add_command(label="Cut", command=myfunc5)
m5.add_command(label="Copy", command=myfunc6)
m5.add_separator()
m5.add_command(label="Paste", command=myfunc7)
m5.add_command(label="Find", command=myfunc8)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Code", menu=m5)

m6 = Menu(mainmenu, tearoff=0)
m6.add_command(label="Cut", command=myfunc5)
m6.add_command(label="Copy", command=myfunc6)
m6.add_separator()
m6.add_command(label="Paste", command=myfunc7)
m6.add_command(label="Find", command=myfunc8)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Refactor", menu=m6)

m7 = Menu(mainmenu, tearoff=0)
m7.add_command(label="Cut", command=myfunc5)
m7.add_command(label="Copy", command=myfunc6)
m7.add_separator()
m7.add_command(label="Paste", command=myfunc7)
m7.add_command(label="Find", command=myfunc8)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Run", menu=m7)

m8 = Menu(mainmenu, tearoff=0)
m8.add_command(label="Cut", command=myfunc5)
m8.add_command(label="Copy", command=myfunc6)
m8.add_separator()
m8.add_command(label="Paste", command=myfunc7)
m8.add_command(label="Find", command=myfunc8)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Windows", menu=m8)


m9 = Menu(mainmenu, tearoff=0)
m9.add_command(label="Help", command=help)
m9.add_command(label="Rate us", command=rate)
m9.add_command(label="UR Frinend Divya", command=divya)
mainmenu.add_cascade(label="Help", menu=m3)
root.config(menu=mainmenu)

root.mainloop()