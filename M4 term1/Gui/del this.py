from tkinter import*

root=Tk()
root.title('Login test')

Label(root,text='Please Login',bg='peach puff')\
    .grid(row=0,columnspan=2,sticky=NSEW)
Label(root,text='Username : ',justify=LEFT)\
    .grid(row=1,column=0)
Label(root,text='Password : ',justify=LEFT)\
    .grid(row=2,column=0)

username = StringVar()
Entry(root,textvariable=username,justify=RIGHT)\
    .grid(row=1,column=1)
password = StringVar()
Entry(root,textvariable=password,justify=RIGHT,show='*')\
    .grid(row=2,column=1)

textshow = StringVar()
def Login ():
    if username.get() == 'Next' and password.get() == 'next123':
        textshow.set('Welcome')
        labeltextshow = Label(root,textvariable=textshow,)
        labeltextshow.grid(row=4,columnspan=2,sticky=NSEW)
    else:
        textshow.set('Try Again')
        labeltextshow = Label(root,textvariable=textshow,)
        labeltextshow.grid(row=4,columnspan=2,sticky=NSEW)
        
        

Button(root,text='Login',command=Login)\
    .grid(row=3,columnspan=2,sticky=NSEW)

    

root.mainloop()
