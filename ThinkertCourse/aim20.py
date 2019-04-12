from tkinter import *
def upload():
    statusvar.set("Busy...")
    import time
    sbar.update()
    time.sleep(2)
    statusvar.set("Ready")
root = Tk()
root.geometry("844x566")
root.title("Status bar turorial")
statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)
Button(root,text="Upload", command=upload).pack()
root.mainloop()
