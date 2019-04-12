from tkinter import *
root = Tk()
root.geometry("644x344")
def setvals():
    print("it's works")
Label(root, text="Welcome to vishal travels", font="times 12 bold", pady=20).grid(row=0, column=3)
name= Label(root, text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency = Label(root,text="Emergency")
bill = Label(root,text="bill")
payementmode = Label(root,text="paymentmode")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
bill.grid(row=5,column=2)
payementmode.grid(row=6,column=2)

namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
billvalue=StringVar()
payementmodevalue=StringVar()
foodservicevalue=IntVar()

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
billentry=Entry(root,textvariable=billvalue)
payementmodeentry=Entry(root,textvariable=payementmodevalue)


nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
billentry.grid(row=5, column=3)
payementmodeentry.grid(row=6, column=3)


foodservicevalue= Checkbutton(text="Want to prebook your meals?", variable= foodservicevalue)
foodservicevalue.grid(row=7,column=3)


Button(text="Submit to Vishal Travels", command=setvals).grid(row=8, column=3)

root.mainloop()