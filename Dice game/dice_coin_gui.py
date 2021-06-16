import random
from tkinter import *

top = Tk() 
top.geometry('650x400') 
top.title("Dice/Coin Simulator")

label = Label(top,text='',font=('Arial',250))
label.place(x=225,y=120)

l1 = Label(top,text='Dice/Coin Simulation Game',font=('Arial',10))
l1.place(x = 225, y=20)

def dice():
	b = Button(top,text='Roll Unbiased Dice',foreground='blue',command =dice_unbiased)
	b.place(x=50,y=80)

	b1 = Button(top,text='Roll Biased Dice',foreground='red',command =dice_biased)
	b1.place(x=200,y=80)

def coin():
	b = Button(top,text='Flip Unbiased Coin',foreground='blue',command =coin_unbiased)
	b.place(x=350,y=80)

	b1 = Button(top,text='Flip Biased Coin',foreground='red',command =coin_unbiased)
	b1.place(x=500,y=80)


def coin_unbiased():
	s=('\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685')
	label.configure(text=f'{random.choice(s)}')
	label.pack()

	return 0

def coin_biased():
	s=('\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685')
	label.configure(text=f'{random.choice(s)}')
	label.pack()

	return 0

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

diceb = Button(top,text='Roll Dice',foreground='blue',command =dice)
diceb.place(x=150,y=50)

coinb = Button(top,text='Flip Coin',foreground='red',command =coin)
coinb.place(x=450,y=50)

top.mainloop()


