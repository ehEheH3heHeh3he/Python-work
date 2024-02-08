
from tkinter import *
from tokenize import String
root = Tk()
root.geometry('1100x800+400+0')
root.option_add("*font",'PSL-omyim=30')
root.title('work')


menu = {'apple':20,'banana':30,'orenge':200,'melon':10}
price = StringVar()
price.set(f'price')
totalmenu = StringVar()
totalmenu.set(f'selected menu')
totalprice = 0
allmenu = ''



def click1():
    global allmenu,totalmenu,menu,price,totalprice
    menuitem = button4.cget('text')
    totalprice += menu[menuitem]
    price.set(f'selected menu = {totalprice} $')
    allmenu += menuitem+' price '+str(menu[menuitem])+' $\n'
    totalmenu.set(f'selected menu : \n{allmenu}')

def click2():
    global allmenu,totalmenu,menu,price,totalprice
    menuitem = button3.cget('text')
    totalprice += menu[menuitem]
    price.set(f'selected menu = {totalprice} $')
    allmenu += menuitem+' price '+str(menu[menuitem])+' $\n'
    totalmenu.set(f'selected menu : \n{allmenu}')
    
def click3():
    global allmenu,totalmenu,menu,price,totalprice
    menuitem = button2.cget('text')
    totalprice += menu[menuitem]
    price.set(f'selected menu = {totalprice} $')
    allmenu += menuitem+' price '+str(menu[menuitem])+' $\n'
    totalmenu.set(f'selected menu : \n{allmenu}')

def click4():
    global allmenu,totalmenu,menu,price,totalprice
    menuitem = button1.cget('text')
    totalprice += menu[menuitem]
    price.set(f'selected menu = {totalprice} $')
    allmenu += menuitem+' price '+str(menu[menuitem])+' $\n'
    totalmenu.set(f'selected menu : \n{allmenu}')

def finish():
    root.destroy
    root2 = Tk()
    root2.title('totalpoints')
    Label(root2,text=f'Total point :  {totalprice} ',fg= 'purple',width = 34).pack()
    root2.mainloop()   
    

photo1 = PhotoImage(file='steak.png')
photo2 = PhotoImage(file='spagetti.png')
photo3 = PhotoImage(file='soup.png')
photo4 = PhotoImage(file='salmon.png')
label1 = Label(text = '   question',bg = 'peach puff')
label2 = Label(text = '      Major ',bg = 'peach puff')
label3 = Label(text = '      SPSM',bg = 'peach puff')
label_space = Label(text = '     ')
button4 = Button(text = 'apple',bg = 'turquoise',image=photo1,compound=TOP,command=click1)
button3 = Button(text = 'banana',bg = 'red',image=photo2,compound=TOP,command=click2)
button2 = Button(text = 'orenge',bg = 'blue',image=photo3,compound=TOP,command=click3)
button1 = Button(text = 'melon',bg = 'orange',image=photo4,compound=TOP,command=click4)




label1.grid(row=0,column=0,ipadx=520)
label2.grid(row=1,column=0,ipadx=520)
label_space.grid(row=2,column=0,ipadx=300,ipady=140)
label3.grid(row=3,column=0,ipadx=520)

button4.place(x=0,y=58,)
button3.place(x=270,y=58)
button2.place(x=540,y=58)
button1.place(x=810,y=58)



all = Button(textvariable=totalmenu,fg='purple',width=32,)
all.grid(row=5,columnspan=5)

btn_finish = Button(textvariable=totalprice ,fg='red',command=finish)
btn_finish.grid(row=6,column=0)





root.mainloop()