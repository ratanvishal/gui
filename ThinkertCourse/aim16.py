from tkinter import *
import tkinter.messagebox as tsmg
root = Tk()
root.geometry("855x566")
root.title("radio button")
def order():
    tsmg.showinfo("Order Received!", f"We have received your order for {var.get()}. Thanks for ordering")
var = StringVar()
var.set("Radio")
Label(root, text="What would you like to have sir?", font = "lucida 19 bold",
      justify=LEFT, padx=14). pack()
radio = Radiobutton(root, text="Dosa", padx=14, variable=var, value="Dosa").pack(anchor="w")
radio = Radiobutton(root, text="Idly", padx=14, variable=var, value="Idly").pack(anchor="w")
radio = Radiobutton(root, text="Paratha", padx=14, variable=var, value="paratha").pack(anchor="w")
radio = Radiobutton(root, text="samosa", padx=14, variable=var, value="samosa").pack(anchor="w")
radio = Radiobutton(root, text="wada", padx=14, variable=var, value="wada").pack(anchor="w")
Button(text="Order Now", command=order).pack()


root.mainloop()