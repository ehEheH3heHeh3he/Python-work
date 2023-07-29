# import requests

# url = 'https://notify-api.line.me/api/notify'
# token = 'UNI2cO7AxaSTjzRpu3gmNEaf6nJCTlwZS6wmHfcC7nz'
# headers = {'Authorization':'Bearer '+token}

# msg = {'oof'}
# while True:
#     requests.post(url=url, headers=headers, data={'message':msg})


from tkinter import*
from tkinter import messagebox

root = Tk()
root.title('Radiobutton test')

col_n = 2
label1 = Label(root,text = 'จังหวัดที่อยากไปมากสุด',fg = 'black',bg = 'gold')
label1.grid(row = 0,column=0,columnspan=col_n,sticky=NSEW)

list_travel = ['กทม','ชลบุรี','เลย','พังงา','ภูเก็ต','เชียงใหม่']
value = ['1','2','3','4','5','6']

show = StringVar(value='ผลลัพธ์')
vg = StringVar()
vg.set(0)
def onclick():
    show.set(f'คุณได้เลือกจักหวัด\n{vg.get()}')

for i in range(len(list_travel)):
    rd = Radiobutton(root,text = list_travel[i],variable=vg,value=value[i],width=10,indicatoron=True,command=onclick)
    rd.grid(row=(i//col_n)+1,column=i%col_n,sticky=NSEW)

label2 = Label(root,textvariable= show,fg = 'black',bg = 'gold',width=20,height=2,wraplength=500)
label2.grid(row = 0,column=0,columnspan=col_n,sticky=NSEW)



def exit():
    confirm = messagebox.askquestion('ยืนยัน','คุณต้องการออกจากโปรแกรมใช่หรือไม่')
    if confirm == 'yes':
        root.destroy

def show_warning() :
    messagebox.showwarning('warning','บันทึกข้อมูลเรียบร้อยแล้ว')

def show_info():
    messagebox.showinfo('รายระเอียด','ทดสอบmesegebox')

btn1 = Button(root, text='ออก', command=exit)
btn1.grid(row=5,column=0,sticky=NSEW)
btn2 = Button(root, text='save', command=show_warning)
btn2.grid(row=5,column=1,sticky=NSEW)
btn3 = Button(root, text='info', command=show_info) 
btn3.grid(row=5,column=2,sticky=NSEW)

root.mainloop()