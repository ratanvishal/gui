from tkinter import *
root=Tk()
root.geometry("733x433")
f1=Frame(root, bg="blue", borderwidth=10, relief=SUNKEN)
f1.pack(side=LEFT,fill="y")
f2=Frame(root, bg="red", borderwidth=10, relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l=Label(f1,text="project tkinter")
l.pack(pady=142)
l=Label(f2,text="Welcome to subline-text", font="times 20 bold",fg="green")
l.pack(pady=20)
root.mainloop()
