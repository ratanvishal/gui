from tkinter import *
import os
from PIL import Image, ImageTk

mahmudul_root = Tk()

mahmudul_root.geometry("533x433")
# photo = PhotoImage(file="1.png")

# For Jpg Images

image = Image.open("2.jpg")
photo = ImageTk.PhotoImage(image)

varun_label = Label(image=photo)
varun_label.pack()



mahmudul_root.mainloop()
