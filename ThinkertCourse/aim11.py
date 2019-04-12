from tkinter import *
def vishal(event):
    print(f"you clicked on the button at {event.x},{event.y}")

root = Tk()
root.title("Vishal's Events")
root.geometry("844x433")

widget = Button(root, text='click me please')
widget.pack()

widget.bind('<Button1-1>', vishal)
widget.bind('<Double1>', quit)

root.mainloop()

# 16ram, 512ssd,i7 8th generation
# 13.3, 14"