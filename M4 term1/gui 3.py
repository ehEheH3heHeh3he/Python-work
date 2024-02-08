# from re import T
from tkinter import *
root = Tk()
root.geometry('300x300+1000+300')

button1 = Button(text='Bind event')
button1.pack(expand=True)

def on_click(event):
    event.widget['text']='on_click'
def right_click(event):
    event.widget['text']='right_click'
def mouse_enter(event):
    event.widget['text']='mouse_enter'
def mouse_leave(event):
    event.widget['text']='mouse_leave'
def doubleclick(event):
    event.widget['text']='doubleclick'

button1.bind('<Button-1>',on_click)
button1.bind('<Button-3>',right_click)
button1.bind('<Enter>',mouse_enter)
button1.bind('<Leave>',mouse_leave)
button1.bind('<Double-1>',doubleclick)




root.mainloop()