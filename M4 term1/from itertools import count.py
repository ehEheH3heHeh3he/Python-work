from tkinter import*

import requests
url = 'https://notify-api.line.me/api/notify'
token = 'GPMEi8gvjEf6J60eUvT2uKGKkQ5801ZD9KVwlQ71gP1'
headers = {'Authorization':'Bearer '+token}

root = Tk()
root.title('Bhumi Caculator')

input = StringVar()
empty = Entry(root, textvariable=input, width=50,bd = 0, bg='#f453ad')
empty.grid(row=0,column=0,ipady=10)

buaklopkoonharn = ''

def button_click(number):
    global buaklopkoonharn
    buaklopkoonharn = buaklopkoonharn + str(number)
    input.set(buaklopkoonharn)

def button_clear(): 
    global buaklopkoonharn 
    buaklopkoonharn = ''
    input.set('')

def button_equal():
    global buaklopkoonharn,result
    result = str(eval(buaklopkoonharn))
    input.set(result)
    buaklopkoonharn = ''
    msg = {'คำตอบของตัวเลขที่ป้อน :'+result}
    requests.post(url=url, headers=headers, data={'message':msg})

frameofbutton = Frame(root, width=300, height=300, bg='misty rose')
frameofbutton.grid()

one = Button(frameofbutton, text = '1', fg = '#f453ad', width = 10, height = 3, bd = 0, bg = 'misty rose', command = lambda: button_click(1))
one.grid(row = 3, column = 0)
 
two = Button(frameofbutton, text = '2', fg = '#f453ad', width = 10, height = 3, bd = 0, bg = 'misty rose', command = lambda: button_click(2))
two.grid(row = 3, column = 1)
 
three = Button(frameofbutton, text = '3', fg = '#f453ad', width = 10, height = 3, bd = 0, bg = 'misty rose', command = lambda: button_click(3))
three.grid(row = 3, column = 2)

four = Button(frameofbutton, text = '4', fg = '#f453ad', width = 10, height = 3, bd = 0, bg = 'misty rose', command = lambda: button_click(4))
four.grid(row = 2, column = 0)
 
five = Button(frameofbutton, text = '5', fg = '#f453ad', width = 10, height = 3, bd = 0, bg = 'misty rose', command = lambda: button_click(5))
five.grid(row = 2, column = 1)
 
six = Button(frameofbutton, text = '6', fg = '#f453ad', width = 10, height = 3, bd = 0, bg = 'misty rose', command = lambda: button_click(6))
six.grid(row = 2, column = 2)

seven = Button(frameofbutton, text = '7', fg = '#f453ad', width = 10, height = 3, bd = 0, bg = 'misty rose', command = lambda: button_click(7))
seven.grid(row = 1, column = 0)
 
eight = Button(frameofbutton, text = '8', fg = '#f453ad', width = 10, height = 3, bd = 0, bg = 'misty rose', command = lambda: button_click(8))
eight.grid(row = 1, column = 1)
 
nine = Button(frameofbutton, text = '9', fg = '#f453ad', width = 10, height = 3, bd = 0, bg = 'misty rose', command = lambda: button_click(9))
nine.grid(row = 1, column = 2)

zero = Button(frameofbutton, text = '0', fg = '#f453ad', width = 21, height = 3, bd = 0, bg = 'misty rose', command = lambda: button_click(0))
zero.grid(row = 4, column = 0, columnspan = 3)
 
equal = Button(frameofbutton, text = '=', fg = 'white', width = 10, height = 3, bd = 0, bg = 'pink', command = lambda: button_equal())
equal.grid(row = 3, column = 3)

plus = Button(frameofbutton, text = '+', fg = 'white', width = 10, height = 3, bd = 0, bg = 'pink', command = lambda: button_click('+'))
plus.grid(row = 2, column = 3)

minus = Button(frameofbutton, text = '-', fg = 'white', width = 10, height = 3, bd = 0, bg = 'pink', command = lambda: button_click('-'))
minus.grid(row = 1, column = 3)

clear = Button(frameofbutton, text = 'C', fg = 'white', width = 32, height = 3, bd = 0, bg = 'pink', command = lambda: button_clear())
clear.grid(row = 0, column = 0, columnspan = 3)

root.mainloop()