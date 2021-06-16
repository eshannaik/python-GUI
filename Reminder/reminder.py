from tkinter import *
from tkinter import messagebox 
import time
from playsound import playsound

top = Tk()
top.geometry("500x200")
top.title("Remainder")

hour=StringVar()
mins=StringVar()
sec=StringVar()

global times,counts,countr
countr = 0
counts = 0
times = 7200

d = Label(top,text='Reminder App', font=('Arial',20,'bold'))
d.pack()

r = Label(top,text='',font=('Arial',70))

l = Label(top,text='',font=('Arial',10))

def clock():
	t = time.strftime("%I:%M:%S %p")
	l.config(text= t)
	l.after(1000, clock)

def start():
	global times,counts,countr
	hour = times // 3600
	x = times % 3600
	mins = x // 60
	sec = times % 60
	timer = '{:02d}:{:02d}:{:02d}'.format(hour,mins,sec)
	r.config(text = timer)

	if ((times % 1200 == 0) and (times!=0) and (times!=7200)):
		playsound("C:/Users/eshan/Desktop/alarm_beep.mp3")
		messagebox.showinfo(title="Eyes",message="Look Away, get up for 1 to 2 minutes(music will stop in 4 seconds)")

	if ((times % 3600 == 0) and (times!=0) and (times!=7200)):
		playsound("C:/Users/eshan/Desktop/alarm_beep.mp3")
		messagebox.showinfo(title="Water",message="Drink 250ml of Water(music will stop in 4 seconds)")

	if(times == 0 and (times!=7200)):
		playsound("C:/Users/eshan/Desktop/alarm_beep.mp3")
		messagebox.showinfo(title="Leave",message="Get up for 15 to 45 mins(music will stop in 4 seconds)")

	if(times < -1 or counts == 1):
		counts = 0
		return 0 

	if(countr == 1):
		countr = 0
		return 0

	times =times - 1
	r.after(1000,start)

def stop():
	global times, counts
	counts = counts + 1

def reset():
	global times,countr
	times = 7200
	countr = countr + 1


r.place(x=65,y=40)
l.place(x=420,y=10)	
clock()

startb = Button(top,text='Start',command=start)
startb.place(x = 80 , y=160)

stopb = Button(top,text='Stop', command=stop)
stopb.place(x = 225 , y=160)

resetb = Button(top,text='Reset',command =reset)
resetb.place(x = 375 , y=160)

top.mainloop()