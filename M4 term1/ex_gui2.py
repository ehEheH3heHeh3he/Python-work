import tkinter as tk

frame = tk.Tk()
frame.title("BMI CLACULATOR")
frame.geometry('400x200')

def printInput():
	inp = str(float(inputtxt2.get(1.0, tk.END))/(float(inputtxt.get(1.0, tk.END))**2))
	lbl.config(text = "BMI : "+inp )

label1 = tk.Label(text = '  Hight :  ',bg = 'peach puff')
inputtxt = tk.Text(frame,height = 1,width = 20)
label2 = tk.Label(text = 'Weight : ',bg = 'peach puff')
inputtxt2 = tk.Text(frame,height = 1,width = 20)

label1.grid(row=0,column=0)
inputtxt.grid(row=0,column=1)
label2.grid(row=1,column=0)
inputtxt2.grid(row=1,column=1)

printButton = tk.Button(frame,text = "Print",command = printInput)
printButton.grid(row=2,column=0)

lbl = tk.Label(frame, text = "")
lbl.grid(row=3,column=0)

frame.mainloop()