from datetime import datetime
from time import time
from tkinter import*


root = Tk()
teamacount= 0
teambcount = 0
totalcount= 0

tvteama= IntVar()
tvteamb= IntVar()
tvtotal = StringVar()

tvtotal.set(f'total score both team = {totalcount}')

photo1 = PhotoImage(file='liverpool.png')
photo2 = PhotoImage(file='manu.png')

dtdate = datetime.now().strftime('%d/%m/%Y')
dttime = datetime.now().strftime('%H:%M:%S')

label=Label(root, text='Batminton Score Board', fg='white', bg='black')
label.grid(row=0,columnspan=2,sticky=NSEW)
btn1=Button(root, text='Team_A', image=photo1, compound=TOP, fg='green', padx=70)
btn1.grid(row=1,column=0, ipady=20,sticky=NSEW)
btn2=Button(root, text='Team_B', image=photo2, compound=TOP, fg='red', padx=50)
btn2.grid(row=1,column=1, ipady=20,sticky=NSEW)
label1=Label(root, textvariable=tvteama, bg='lightblue')
label1.grid(row=2, column=0, sticky=NSEW)
label2=Label(root, textvariable=tvteamb, bg='pink')
label2.grid(row=2,column=1, sticky=NSEW)
label3=Label(root, textvariable=tvtotal, bg='gold')
label3.grid(row=7,columnspan=2, sticky=NSEW)

def on_click(e):
    global teamacount,teambcount,totalcount
    score = e.widget['text']
    if score == 'Team_A':
        teamacount+=1
        tvteama.set(teamacount)
    else:
        teambcount+=1
        tvteamb.set(teambcount)
        
    totalcount+=1
    tvtotal.set(f'both team score = {totalcount}')

def right_click(e):
    global teamacount,teambcount,totalcount
    score = e.widget['text']
    if score == 'Team_A':
        teamacount-=1
        tvteama.set(teamacount)

    else:
        teambcount-=1
        tvteamb.set(teambcount)
    totalcount-=1
    tvtotal.set(f'both team score = {totalcount}')
btn1.bind('<Button-1>',on_click)
btn1.bind('<Button-3>',right_click)
btn2.bind('<Button-1>',on_click)
btn2.bind('<Button-3>',right_click)

label4=Label(root,text=dttime,fg='white',bg='blue')
label4.grid(row=3,columnspan=2,sticky=NSEW)
label5=Label(root,text=('Date '+dtdate),bg='white')
label5.grid(row=6,columnspan=2,sticky=NSEW)
def tick():
    global curtime
    curtime = datetime.now().time()
    ftime = curtime.strftime('%H:%M:%S')

    label4.config(text='time : '+ftime)
    label4.after(1000,tick)
tick()

label6=Label(root,text='countdown 45:00 min',fg='white',bg='red')
label6.grid(row=5,columnspan=2,sticky=NSEW)
t=45*60
def countdown():
    global timer,mins,secs,t,teamacount,teambcount
    t-=1
    mins,secs = divmod(t,60)
    timer = '{:02d}:{:02d}'.format(mins,secs)

    label6.config(text=('countdown : '+timer))
    label6.after(1000,countdown)
countdown()

message_line=(f'team A result{teamacount} and team B {teambcount}')
def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload)
def _lineNotify(payload,file=None) :
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = 'wwu3yy2EfbkNIm6ozl3l49K9Fn5H4ELF5BwXfpPR3yN'
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url=url,headers=headers,data=payload,files=file)
def line():
    global message_line
    message_line=(f'team A result{teamacount} and team B {teambcount}')
    print(message_line)

    lineNotify(message_line)
btn4=Button(root,text='end of the game and sending results',fg ='red',command=line)
btn4.grid(row=8,columnspan=2,sticky=NSEW)

root.mainloop()