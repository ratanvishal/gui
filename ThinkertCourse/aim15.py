from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("844x655")
root.title("slider tutorial")
def getdollar():
    print(f"We have credited {myslider2.get()} dollars to your bank account")
    tmsg.showinfo("Amount Creadited", f"We have credited {myslider2.get()} dollars to your bank account")



Label(root, text="How many dollars do you want?").pack()
myslider2 = Scale(root, from_=0, to_=100, orient=HORIZONTAL, tickinterval=25)
myslider2.pack()

Button(root, text="Get Dollars!", padx=10, command=getdollar).pack()
root.mainloop()