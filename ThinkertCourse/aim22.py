from tkinter import *
root=Tk()
root.geometry("1080x1080")
root.title("Code with vishal Title of my gui")
root.wm_iconbitmap("1.ico")
root.configure(bg="black")
width=root.winfo_screenmmwidth()
height=root.winfo_screenmmheight()
print((f"{width}x{height}"))
Button(text="close", command=root.destroy).pack()
root.mainloop()