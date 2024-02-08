from cProfile import label
from pydoc import TextRepr
from tkinter import*
from turtle import onclick, st

root = Tk()
root.title('checkbox test')

label1 = Label(root,text = 'แบบสำรวจความต้องการ',fg = 'black',bg = 'gold')
label1.grid(row = 0,column=0,columnspan=2,sticky=NSEW)

boolckeck1 = BooleanVar()
check1 = Checkbutton(root,text='ภาษาอังกฤษ',variable=boolckeck1)
check1.grid(row=1,column=0,sticky=NSEW)

valuecheck = BooleanVar()
check2 = Checkbutton(root,text = 'python',variable = valuecheck)
check2.grid(row=1,column=1,sticky=NSEW)

show = StringVar(value='')
lable2 = Label(root,textvariable=show,fg = 'red',bg='lightblue')
lable2.grid(row=3,column=0,columnspan=2,sticky=NSEW)

def onclick():  
    a = int(valuecheck.get())   #boolckeck1.get()
    b = int(valuecheck.get())
    show.set(f'ความต้องการภาษาอังกฤษมีค่าเป็น{a}\nความต้องการpythonมีค่าเป็น{b}')

def reset():
    global show ,boolckeck1,valuecheck
    show.set('')

    boolckeck1 = BooleanVar()
    check1 = Checkbutton(root,text='ภาษาอังกฤษ',variable=boolckeck1)
    check1.grid(row=1,column=0,sticky=NSEW)

    valuecheck = BooleanVar()
    check2 = Checkbutton(root,text = 'python',variable = valuecheck)
    check2.grid(row=1,column=1,sticky=NSEW)

btn1 = Button(root,text='แสดงผลการสำรวจ',fg='brown',command=onclick)
btn1.grid(row=2,column=1,sticky=NSEW)

btn2 = Button(root,text='reset',fg='brown',command=reset)
btn2.grid(row=2,column=0,sticky=NSEW)

root.mainloop()