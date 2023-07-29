from tkinter import*
from tkinter import ttk

root = Tk()
root.title('combobox test')

Label(root,text='โปรแกมสูตรคูณ',fg='gold',bg = 'black')\
    .grid(row=0,column=0,columnspan=2,sticky=NSEW)
Label(root,text='ตัวเลขที่1',fg='gold',justify=LEFT)\
    .grid(row=1,column=0,columnspan=2,sticky=NSEW)
Label(root,text='ตัวเลขที่2',fg='gold',justify=LEFT)\
    .grid(row=2,column=0,columnspan=2,sticky=NSEW)

num1 = StringVar(value='ระบุตัวเลขที่1')
value_num = [1,2,3,4,5,6,7,8,9,10,11,12] #set in combobox
cb1 = ttk.Combobox(root,values=value_num,textvariable=num1,justify=CENTER,width=15,state='readonly')
cb1.grid(row=1,column=1,sticky=NSEW)

num2 = StringVar(value='ระบุตัวเลขที่2')
value_num2 = list(range(1,13))
cb2 = ttk.Combobox(root,values=value_num2,textvariable=num2,justify=CENTER,width=15,state='readonly')
cb2.grid(row=2,column=1,sticky=NSEW)

show = IntVar(value='ผลลัพธ์')
def onclick():
    a,b = num1.get(),num2.get()
    if a == 'ระบุตัวเลขที่1'and b == 'ระบุตัวเลขที่2' :
        show.set('กรุณาระบุตัวเลข')
    elif a == 'ระบุตัวเลขที่1'or b == 'ระบุตัวเลขที่2' :
        show.set('กรุณาระบุตัวเลขให้ครบ')
    else:
        a,b = int(num1.get()),int(num2.get())
        c = a*b
        label1.config(bg='red',fg='white')
        show.set(f'{a}*{b}={c}')
        print((f'{a}*{b}={c}'))
btn1 = Button(root,text='คำณวน',fg='brown',command=onclick)
btn1.grid(row=3,column=1,sticky=NSEW)
label1=Label(root,fg='blue',bg = 'lightblue',textvariable=show)
label1.grid(row=4,columnspan=2,sticky=NSEW)
def onclick2():
    show.set('-')
    num1.set('ระบุตัวเลขที่1')
    num2.set ('ระบุตัวเลขที่2')

btn2 = Button(root,text='reset',fg='brown',command=onclick2)
btn2.grid(row=5,column=1,sticky=NSEW)


root.mainloop()