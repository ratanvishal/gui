from tkinter import *
root=Tk()
root.geometry("500x400")
root.minsize(500,400)
root.maxsize(500,400)
root.title("vishal gui")
title_lable=Label(text="ready", bg="black", fg="red", font="times 20 bold")

title_lable.pack(side=BOTTOM, fill=Y, padx=10, pady=10)
root.mainloop()