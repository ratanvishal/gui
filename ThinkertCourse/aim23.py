from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
              value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
        scvalue.set(value)
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
root = Tk()

root.geometry("844x655")
root.title("calculator")
root.wm_iconbitmap("1.ico")
# root.minsize("")
# root.maxsize("")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, bg="black", fg="red", textvar=scvalue, font="times 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="grey")
b = Button(f, text="9", bg="black", fg="red", padx=28, pady=22, font="times 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)


b = Button(f, text="8", bg="black", fg="red", padx=28, pady=22, font="times 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="7", bg="black", fg="red", padx=28, pady=22, font="times 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="6", bg="black", fg="red", padx=28, pady=22, font="times 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)


b = Button(f, text="5", bg="black", fg="red", padx=28, pady=22, font="times 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="4", bg="black", fg="red", padx=28, pady=22, font="times 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="3", bg="black", fg="red", padx=28, pady=22, font="times 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)


b = Button(f, text="2", bg="black", fg="red", padx=28, pady=22, font="times 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="1", bg="black", fg="red", padx=28, pady=22, font="times 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="0", bg="black", fg="red", padx=32, pady=22, font="times 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)


b = Button(f, text="-", bg="black", fg="red", padx=28, pady=22, font="times 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="*", bg="black", fg="red", padx=28, pady=22, font="times 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="C", bg="black", fg="red", padx=27, pady=22, font="times 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)


b = Button(f, text="+", bg="black", fg="red", padx=28, pady=22, font="times 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="/", bg="black", fg="red", padx=28, pady=22, font="times 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text=".", bg="black", fg="red", padx=26, pady=22, font="times 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)


b = Button(f, text="=", bg="black", fg="red", padx=25, pady=22, font="times 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="%", bg="black", fg="red", padx=25, pady=22, font="times 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()