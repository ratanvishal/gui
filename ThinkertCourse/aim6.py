from tkinter import *
root = Tk()
root.geometry("833x455")
def getvals():
    print(f"the username is {uservalue.get()}")
    print(f"the password is {passvalue.get()}")
root.title("email")
user = Label(root, text="username", borderwidth=4, bg="yellow")
password = Label(root, text="password", borderwidth=4, bg="blue", fg="white")
user.grid(row=1)
password.grid(row=2)

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue, borderwidth=4, bg="pink", fg="blue")
passentry = Entry(root, textvariable=passvalue, borderwidth=4, bg="red", fg="yellow")

userentry.grid(row=1, column=1)
passentry.grid(row=2, column=1)

Button(text="Submit", bg="black", fg="white", command=getvals).grid()

root.mainloop()
