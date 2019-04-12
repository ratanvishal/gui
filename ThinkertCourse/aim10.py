tyyuuu
from tkinter import *

def harry(event):
    print(f"You clicked on the button at {event.x}, {event.y}")

root = Tk()
root.title("Events in Tkinter")
root.geometry("644x334")

widget = Button(root, text='Click me please')
widget.pack()

widget.bind('<Button-1>', harry)
widget.bind('<Double-1>', quit)

root.mainloop()


# gl==72000+18%=84960 online-85990 gk-1030
# tuff 017t=92110   online-93990 t-1880
# tuff 335t-81330   online-83990 t-2660
