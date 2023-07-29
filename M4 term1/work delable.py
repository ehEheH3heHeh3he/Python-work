from tkinter import *

root = Tk()

root.title("Homework-GUI")
root.geometry("600x500+350+150")

label1 = Label(text="NAME:",bg='yellow')
label1.grid(row=0, column=0, ipadx=300, ipady=15)

label2 = Label(text="MAJOR",bg="lightgreen")
label2.grid(row=1, column=0, ipadx=300, ipady=15)

label_space = Label()
label_space.grid(row=2, column=0, ipady=55)

label3 = Label(bg="pink")
label3.place(x=0, y=103, height=110, width=110)

label4 = Label(bg="red")
label4.place(x=170, y=103, height=110, width=110)

label5 = Label(bg="pink")
label5.place(x=340, y=103, height=110, width=110)

label6 = Label(bg="red")
label6.place(x=490, y=103, height=110, width=110)

label7 = Label(text="SPSM",bg="white")
label7.grid(row=3, column=0, ipadx=300, ipady=15)

label8 = Label(text="OK",bg="black", fg="white")
label8.grid(row=4, column=0, ipadx=150, ipady=15, pady=10)


root.mainloop()