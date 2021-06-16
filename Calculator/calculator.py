from tkinter import * 

top = Tk()
top.geometry("425x357")
top.resizable('0','0')
top.title('Calculator')

def btn_click(text):
	global exp
	exp = exp + str(text)
	input_text.set(exp)

def bt_clear(): 
    global exp
    exp = "" 
    input_text.set("")

def bt_equal():
    global exp
    result = str(eval(exp)) 
    input_text.set(result)
    exp = ""

exp =""

input_text = StringVar()

i= Frame (top,width="425",height="250",bd = 4, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
i.pack(side='top')

box = Entry(i,width="200",text=('arial',18,'bold'),textvariable=input_text,bg='#eee',justify='right',bd=2)
box.grid(row='0', column='0')
box.pack(ipady='10')

b = Frame(top,width="425",height="350")
b.pack()

seven = Button(b,height='4',width="10",activebackground='grey',text="7",bd= 4,cursor = "hand2",command=lambda : btn_click(7)).grid(row=0,column=0,padx=1,pady=1)
eight = Button(b,height='4',width="10",activebackground='grey',text="8",bd= 4,cursor = "hand2",command= lambda : btn_click(8)).grid(row=0,column=1,pady=1)
nine = Button(b,height='4',width="10",activebackground='grey',text="9",bd= 4,cursor = "hand2",command= lambda : btn_click(9)).grid(row=0,column=2,pady=1,padx=1)
divide = Button(b,height='4',width="10",activebackground='grey',text="/",bd= 4,cursor = "hand2",command= lambda : btn_click("/")).grid(row=0,column=3,pady=1,padx=1)
clear = Button(b,height='4',width="10",activebackground='grey',text="C",bd= 4,cursor = "hand2",command= lambda : bt_clear()).grid(row=0,column=4,pady=1,padx=1)

six = Button(b,height='4',width="10",activebackground='grey',text="6",bd= 4,cursor = "hand2",command= lambda : btn_click(6)).grid(row=1,column=0,pady=1,padx=1)
five = Button(b,height='4',width="10",activebackground='grey',text="5",bd= 4,cursor = "hand2",command= lambda : btn_click(5)).grid(row=1,column=1,pady=1,padx=1)
four = Button(b,height='4',width="10",activebackground='grey',text="4",bd= 4,cursor = "hand2",command= lambda : btn_click(4)).grid(row=1,column=2,pady=1,padx=1)
multiply = Button(b,height='4',width="10",activebackground='grey',text="*",bd= 4,cursor = "hand2",command= lambda : btn_click("*")).grid(row=1,column=3,pady=1,padx=1)

one = Button(b,height='4',width="10",activebackground='grey',text="1",bd= 4,cursor = "hand2",command= lambda : btn_click(8)).grid(row=2,column=0,pady=1,padx=1)
two = Button(b,height='4',width="10",activebackground='grey',text="2",bd= 4,cursor = "hand2",command= lambda : btn_click(8)).grid(row=2,column=1,pady=1,padx=1)
three = Button(b,height='4',width="10",activebackground='grey',text="3",bd= 4,cursor = "hand2",command= lambda : btn_click(8)).grid(row=2,column=2,pady=1,padx=1)
minus = Button(b,height='4',width="10",activebackground='grey',text="-",bd= 4,cursor = "hand2",command= lambda : btn_click("-")).grid(row=2,column=3,pady=1,padx=1)

zero = Button(b,height='4',width="22",activebackground='grey',text="0",bd= 4,cursor = "hand2",command= lambda : btn_click(8)).grid(row=3,column=0,columnspan=2,pady=1,padx=1)
dot = Button(b,height='4',width="10",activebackground='grey',text=".",bd= 4,cursor = "hand2",command= lambda : btn_click(8)).grid(row=3,column=2,pady=1,padx=1)
plus = Button(b,height='4',width="10",activebackground='grey',text="+",bd= 4,cursor = "hand2",command= lambda : btn_click(8)).grid(row=3,column=3,pady=1,padx=1)
equal = Button(b,height='14',width="10",activebackground='grey',text="=",bd= 4,cursor = "hand2",command= lambda : bt_equal()).grid(row=1,column=4,rowspan=3,pady=1,padx=1)

top.mainloop()
