# import requests

# url = 'https://notify-api.line.me/api/notify'
# token = 'NWrt7tugIlYe9Xwvu7mA5sJT7eznr4NNafDgSzgzOoJ'
# headers = {'Authorization':'Bearer '+token}
# message = ('skldjnbvs')
# spam = 1
# while spam == 1 :
#     requests.post(url=url, headers=headers, data={'message':message})

# import requests
 
# url = 'https://notify-api.line.me/api/notify'
# token = 'qvpqRQ42fzkIxXzZfS8xHmVHungKm9xdlPWqoVQbCpZ'
# headers = {'Authorization':'Bearer '+token}
 
# msg = 'oof'
# requests.post(url=url, headers=headers, data={'message':msg})


import tkinter as tk
  
# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it 
# at label widget
  
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: "+inp)
  
# TextBox Creation
inputtxt = tk.Text(frame,
                   height = 5,
                   width = 20)
  
inputtxt.pack()
  
# Button Creation
printButton = tk.Button(frame,
                        text = "Print", 
                        command = printInput)
printButton.pack()
  
# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()