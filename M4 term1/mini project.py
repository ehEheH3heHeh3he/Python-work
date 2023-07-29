import tkinter as tk
import requests

frame = tk.Tk()
frame.title("Hospital")
frame.geometry('700x200')

url = 'https://notify-api.line.me/api/notify'
token = 'wwu3yy2EfbkNIm6ozl3l49K9Fn5H4ELF5BwXfpPR3yN'
headers = {'Authorization':'Bearer '+token}

queuenum = 0
def printInput():
    global queuenum,ned,user_id,user_name,name
    queuenum +=1
    inp = str(inputtxt.get(1.0,'end-1c'))

    n=int(inp)
    if int(inp) == user_id[n] :
        name = user_name[n]
    else :
        name = 'error '
    msg = {name+'\n'+ned+'Queue : '+str(queuenum)}
    requests.post(url=url, headers=headers, data={'message':msg})

def cm_Surgical() :
    global ned
    ned = 'Surgical Departure '

def cm_Obstretic() :
    global ned
    ned = 'Obstretic Departure '

def cm_Radiology() :
    global ned
    ned = 'Radiology Departure '

def cm_Physical() :
    global ned
    ned = 'Obstretic Departure '

def cm_Ophthalmology() :
    global ned
    ned = 'Ophthalmology Departure '

def cm_Ear() :
    global ned
    ned = 'Ear-Nose-Throat Departure '

def cm_Phycology() :
    global ned
    ned = 'Phycology Departure '


def cm_Other() :
    global ned
    ned = {'Infomation center '}

user_id = [0]
user_name = ['test']
def cm_newacc():
    global user_id
    inpt1 = str(lb_Name.get(1.0,'end-1c'))
    inpt2 = str(lb_Blood.get(1.0,'end-1c'))
    inpt3 = str(lb_Age.get(1.0,'end-1c'))
    inpt4 = str(lb_DC.get(1.0,'end-1c'))

    user_id.append(user_id[-1]+1)
    user_name.append(inpt1)

    msg = {'New registration has been added'+'\nId number : '+str(user_id[-1])+'\nName : '+inpt1+'\nBlood Type : '+inpt2+'\nAge : '+inpt3+'\nCongenital Disease : '+inpt4}
    requests.post(url=url, headers=headers, data={'message':msg})

    print(user_name)
    save_anounce()

def save_anounce():
    info_saved.grid(row=6,column=4,sticky=tk.NSEW,columnspan=7)
info_saved = tk.Label(text='Your infomation is saved!')

label_name = tk.Label(text = '   Insert ID : ',bg = 'misty rose')
inputtxt = tk.Text(frame,height = 1,width = 20)
label = tk.Label(text = '             Select Survice :              ',bg = 'misty rose')

lb_Surgical = tk.Button(text = 'Surgical',bg = 'peach puff',command=cm_Surgical)
lb_Radiology = tk.Button(text = 'Radiology',bg = 'peach puff',command=cm_Radiology)
lb_Obstretic = tk.Button(text = 'Obstretic',bg = 'peach puff',command=cm_Obstretic)
lb_Physical = tk.Button(text = 'Physical Therapy',bg = 'peach puff',command=cm_Physical)
lb_Ophthalmology = tk.Button(text = 'Ophthalmology',bg = 'peach puff',command=cm_Ophthalmology)
lb_Ear = tk.Button(text = 'Ear-Nose-Throat',bg = 'peach puff',command=cm_Ear)
lb_Phycology = tk.Button(text = 'Phycology',bg = 'peach puff',command=cm_Phycology)
lb_Other = tk.Label(text = 'Others : ',bg = 'misty rose')
inputtxt2 = tk.Text(frame,height = 1,width = 20)

lb_newacc = tk.Label(text = '               Application Form               ',bg = 'misty rose')
lb_name = tk.Label(text = 'Name : ',bg = 'misty rose')
lb_Name = tk.Text(frame,height = 1,width = 20)
lb_blood = tk.Label(text = 'Blood : ',bg = 'misty rose')
lb_Blood = tk.Text(frame,height = 1,width = 20)
lb_age = tk.Label(text = 'Age : ',bg = 'misty rose')
lb_Age = tk.Text(frame,height = 1,width = 20)
lb_dc = tk.Label(text = 'Congenital Disease : ',bg = 'misty rose')
lb_DC = tk.Text(frame,height = 1,width = 20)
lb_Submit = tk.Button(text = 'Submit',bg = 'peach puff',command=cm_newacc)

label_name.grid(row=0,column=0,sticky=tk.NSEW)
inputtxt.grid(row=0,column=1,sticky=tk.NSEW)
label.grid(row=1,column=0,sticky=tk.NSEW)

lb_Surgical.grid(row=1,column=1,sticky=tk.NSEW,columnspan=1)
lb_Radiology.grid(row=2,column=0,sticky=tk.NSEW,columnspan=1)
lb_Obstretic.grid(row=2,column=1,sticky=tk.NSEW,columnspan=1)
lb_Physical.grid(row=3,column=0,sticky=tk.NSEW,columnspan=1)
lb_Ophthalmology.grid(row=3,column=1,sticky=tk.NSEW,columnspan=1)
lb_Ear.grid(row=4,column=0,sticky=tk.NSEW,columnspan=1)
lb_Phycology.grid(row=4,column=1,sticky=tk.NSEW,columnspan=1)
lb_Other.grid(row=5,column=0,sticky=tk.NSEW)
inputtxt2.grid(row=5,column=1,sticky=tk.NSEW)

space = tk.Label(text='                    ')
space.grid(row=0,column=3)

lb_newacc.grid(row=0,column=4,sticky=tk.NSEW,columnspan=7)
lb_name.grid(row=1,column=4,sticky=tk.NSEW,columnspan=1)
lb_Name.grid(row=1,column=5,sticky=tk.NSEW,columnspan=6)
lb_age.grid(row=2,column=4,sticky=tk.NSEW,columnspan=1)
lb_Age.grid(row=2,column=5,sticky=tk.NSEW,columnspan=6)
lb_blood.grid(row=3,column=4,sticky=tk.NSEW,columnspan=1)
lb_Blood.grid(row=3,column=5,sticky=tk.NSEW,columnspan=6)
lb_dc.grid(row=4,column=4,sticky=tk.NSEW,columnspan=1)
lb_DC.grid(row=4,column=5,sticky=tk.NSEW,columnspan=6)
lb_Submit.grid(row=5,column=4,sticky=tk.NSEW,columnspan=7)

printButton = tk.Button(frame,text = "Done",command = printInput)
printButton.grid(row=6,column=0,columnspan=2,sticky=tk.NSEW)

frame.mainloop()