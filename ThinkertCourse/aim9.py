from tkinter import *
root=Tk()

canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")
root.title("vishal's gui")
can_widget=Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

can_widget.create_line(0, 0, 800, 400, fill="blue")
can_widget.create_line(0, 400, 800, 0, fill="red")
can_widget.create_rectangle(10, 10, 60, 40,fill="yellow")
can_widget.create_text(200,200, text="the vishal is great", fill="red")
can_widget.create_oval(44,33,800,400)
can_widget.create_bitmap(10,20)
can_widget.create_polygon(200,400,745,680)
can_widget.create_arc(20,50,400,700)
can_widget.create_image(40,500 )
root.mainloop()