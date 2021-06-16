import random
from tkinter import *

top = Tk() 
top.geometry('600x400') 
top.title("Dice Simulator")

label = Label(top,text='',font=('Arial',250))
label.place(x=225,y=120)

l1 = Label(top,text='Dice/Coin Simulation Game',font=('Arial',10))
l1.place(x = 200, y=20)

def dice_unbiased():
	s=('\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685')
	label.configure(text=f'{random.choice(s)}')
	label.pack()

	return 0

def dice_biased():
	s = ('\u2680','\u2680','\u2680','\u2681','\u2682','\u2682','\u2682','\u2682','\u2682','\u2683','\u2683','\u2684','\u2684','\u2684','\u2685','\u2685','\u2685','\u2685','\u2685')
	label.configure(text = f'{random.choice(s)}')
	label.pack()

	return 0

b = Button(top,text='Roll Unbiased Dice',foreground='blue',command =dice_unbiased)
b.place(x=100,y=50)

b1 = Button(top,text='Roll Biased Dice',foreground='red',command =dice_biased)
b1.place(x=400,y=50)

top.mainloop()


