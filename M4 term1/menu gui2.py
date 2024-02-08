from tkinter import *

root = Tk()

menu = {"pizza":1, 'soup':2,"spaketti":3,"burger":69,"frenchfried":4,'salmon':9,'hotdog':9,'salad':9,'steak':9}
totalmenu = StringVar()
price = StringVar()
times = StringVar()

totalmenu.set(f'receiving order')
price.set(f'order:')
allmenu = ''
totalprice = 0

def choose_menu(e):
    global totalmenu, allmenu,menuitem,menu,totalprice
    menuitem = e.widget.cget('text')
    totalprice += menu[menuitem]
    price.set(f"total price{totalprice} $")
    allmenu += menuitem+'price'+str(menu[menuitem])+' $\n'
def mouse_enter(event):
    event.widget['fg']= 'green'
def mouse_leave(event):
    event.widget['fg']= 'black'
def cancel():
    global totalmenu,totalprice,allmenu
    price.set(f'total price = 0 $')
    totalmenu.set(f'start saving new order')
    totalprice = 0
    allmenu = ''
def exit():
    root.destroy()
def bills():
    global totalmenu, allmenu, totalprice
    totalmenu.set("")
   
    print('-----------')
    print(allmenu)
    print('-----------')
    print(f'total {totalprice} $')

restaurant = Label(root,text="จารมิ้มก็เช่นกัน cafe",bg = 'peach puff')
restaurant.grid(row = 0, columnspan=3,sticky=NSEW)
cashier = Label(root,textvariable=times, fg = 'red')
cashier.grid(row=1,columnspan=3,sticky = NSEW)

photo1 = PhotoImage(file='pizza.png')
photo2 = PhotoImage(file='soup.png')
photo3 = PhotoImage(file='spaghetti.png')
photo4 = PhotoImage(file='burger.png')
photo5 = PhotoImage(file='frenchfries.png')
photo6 = PhotoImage(file='salmon.png')
photo7 = PhotoImage(file='hotdog.png')
photo8 = PhotoImage(file='steak.png')
photo9 = PhotoImage(file='salad.png')

menu1 = Button(root, text='pizza', image=photo1, compound=TOP)
menu1.grid(row=1, column=0,sticky=NSEW)
menu2 = Button(root, text='soup', image=photo2, compound=TOP)
menu2.grid(row=1, column=1,sticky=NSEW)
menu3 = Button(root, text='spaketti', image=photo3, compound=TOP )
menu3.grid(row=1, column=2,sticky=NSEW)
menu4 = Button(root, text='burger', image=photo4, compound=TOP)
menu4.grid(row=2, column=0,sticky=NSEW)
menu5 = Button(root, text='frenchfries', image=photo5, compound=TOP)
menu5.grid(row=2, column=1,sticky=NSEW)
menu6 = Button(root, text='salmon', image=photo6, compound=TOP)
menu6.grid(row=2,column=2,sticky=NSEW)
menu7 = Button(root, text='hotdog', image=photo7, compound=TOP)
menu7.grid(row=3,rowspan=3,column=0,sticky=NSEW)
menu8 = Button(root, text='steak', image=photo8, compound=TOP)
menu8.grid(row=3,rowspan=3,column=1,sticky=NSEW)
menu9 = Button(root, text='salad', image=photo9, compound=TOP)
menu9.grid(row=3,rowspan=3,column=2,sticky=NSEW)

tt = Label(root,text='                                            menu list                                              ',bg = 'yellow',fg='red')
tt.grid(row=0,column=4,sticky=NSEW)
svmn = Label(root,text='เริ่มบันทึก',bg='peach puff')
svmn.grid(row=1,column=4,rowspan=4,sticky=NSEW)
c = Button(root,text='cancel',fg='red')
c.grid(row=5,column=4,sticky=NSEW)
# report = Label (root, textvariable=totalmenu,fg='green')
# report.grid(row=4, columnspan=4,sticky=NSEW)
# bill = Label(root, textvariable=price,fg='red',bg='yellow')
# bill.grid(row=5, columnspan=4, sticky=NSEW)
# cancelall = Button(root, text='cancel order', fg= 'red',command = cancel )
# cancelall.grid(row=6,column=0,sticky=NSEW)
# exitall = Button(root, text='Exit',fg='red',command = exit )
# exitall.grid(row=6, column=1, sticky=NSEW)
# billall= Button(root, text= 'save order', fg='purple',command = bills)
# billall.grid(row=6,column=2,sticky=NSEW)

menu1.bind('<Button-1>', choose_menu)
menu2.bind('<Button-1>', choose_menu)
menu3.bind('<Button-1>', choose_menu)
menu4.bind('<Button-1>', choose_menu)
menu5.bind('<Button-1>', choose_menu)
menu6.bind('<Button-1>', choose_menu)
menu1.bind('<Enter>', mouse_enter)
menu2.bind('<Enter>', mouse_enter)
menu3.bind('<Enter>', mouse_enter)
menu4.bind('<Enter>', mouse_enter)  
menu5.bind('<Enter>', mouse_enter)
menu6.bind('<Enter>', mouse_enter)
menu1.bind('<Leave>', mouse_leave)
menu2.bind('<Leave>', mouse_leave)
menu3.bind('<Leave>', mouse_leave)
menu4.bind('<Leave>', mouse_leave)
menu5.bind('<Leave>', mouse_leave)
menu6.bind('<Leave>', mouse_leave)

root.mainloop()