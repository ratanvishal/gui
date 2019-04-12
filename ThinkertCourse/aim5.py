from tkinter import *
root = Tk()
root.geometry("833x533")
# def frame(self,name):
#     self.name=name
def hello():
    print("hello to the graduted schools information")
def name():
    print("your name is vishal")
def roll_number():
    print("roll number is 116011742021")
def class_name():
    print("hollywood vclass is running on")
def school_name():
    print("st.paul's school")
def subjects():
    print("chemisty,physics,maths,c,c++,java,python")
def print_details():
    print("these  r the details of u")

root.title("tkinter Frames")
frame = Frame(root, bg="blue", borderwidth=8, relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")
b1 = Button(frame, fg="red", text="Print Now", command=hello)
b1.pack(side=LEFT, padx=20)
b2 = Button(frame, fg="red", text="tell ur name", command=name)
b2.pack(side=LEFT, padx=20)
b3 = Button(frame, fg="red", text="roll number", command=roll_number)
b3.pack(side=LEFT, padx=20)
b4 = Button(frame, fg="red", text="class name", command=class_name)
b4.pack(side=LEFT, padx=20)
b5 = Button(frame, fg="red", text="school name", command=school_name)
b5.pack(side=LEFT, padx=20)
b6 = Button(frame, fg="red", text="subjects", command=subjects)
b6.pack(side=LEFT, padx=20)
b7 = Button(frame, fg="red", text="Print Now details", command=print_details)
b7.pack(side=LEFT, padx=20)
frame1=(root)
frame1 = Frame(root, bg="red", borderwidth=4, relief=RIDGE)
frame1.pack(side=LEFT, anchor="se")
b1 = Button(frame, fg="red", text="Print Now", command=hello)
b1.pack(side=LEFT, padx=20)
b2 = Button(frame, fg="red", text="tell ur name", command=name)
b2.pack(side=LEFT, padx=20)
b3 = Button(frame, fg="red", text="roll number", command=roll_number)
b3.pack(side=LEFT, padx=20)
b4 = Button(frame, fg="red", text="class name", command=class_name)
b4.pack(side=LEFT, padx=20)
b5 = Button(frame, fg="red", text="school name", command=school_name)
b5.pack(side=LEFT, padx=20)
b6 = Button(frame, fg="red", text="subjects", command=subjects)
b6.pack(side=LEFT, padx=20)
b7 = Button(frame, fg="red", text="Print Now details", command=print_details)
b7.pack(side=LEFT, padx=20)
root.mainloop()