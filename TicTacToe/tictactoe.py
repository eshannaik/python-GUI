from tkinter import *
from tkinter import messagebox

count = 0
board = [["","",""],["","",""],["","",""]]

def board_display():
	global top
	top = Tk()
	top.title("Tik Tac Toe Game")
	top.config(bg="white")

	p = Label(top,text="Player 1(X)",height=3,font=('tisa',14,'bold'))
	p.grid(row=0,column=1)

	b1 = Button(top,text="",height=7,width=10,bg="Black",font=('Arial',14,'bold'),fg="white",command=lambda : v(b1,0,0))
	b2 = Button(top,text="",height=7,width=10,bg="Black",font=('Arial',14,'bold'),fg="white",command=lambda : v(b2,0,1))
	b3 = Button(top,text="",height=7,width=10,bg="Black",font=('Arial',14,'bold'),fg="white",command=lambda : v(b3,0,2))
	b4 = Button(top,text="",height=7,width=10,bg="Black",font=('Arial',14,'bold'),fg="white",command=lambda : v(b4,1,0))
	b5 = Button(top,text="",height=7,width=10,bg="Black",font=('Arial',14,'bold'),fg="white",command=lambda : v(b5,1,1))
	b6 = Button(top,text="",height=7,width=10,bg="Black",font=('Arial',14,'bold'),fg="white",command=lambda : v(b6,1,2))
	b7 = Button(top,text="",height=7,width=10,bg="Black",font=('Arial',14,'bold'),fg="white",command=lambda : v(b7,2,0))
	b8 = Button(top,text="",height=7,width=10,bg="Black",font=('Arial',14,'bold'),fg="white",command=lambda : v(b8,2,1))
	b9 = Button(top,text="",height=7,width=10,bg="Black",font=('Arial',14,'bold'),fg="white",command=lambda : v(b9,2,2))

	b1.grid(row=1,column=0)
	b2.grid(row=1,column=1)
	b3.grid(row=1,column=2)
	b4.grid(row=2,column=0)
	b5.grid(row=2,column=1)
	b6.grid(row=2,column=2)
	b7.grid(row=3,column=0)
	b8.grid(row=3,column=1)
	b9.grid(row=3,column=2)

	q = Button(top,text="Quit Game",font=('Arial',14,'bold'),command=quit)
	q.grid(row = 4, column = 2)

def v(button,r,c):
	global count
	if button["text"]=="":
		if count%2==0:
			button["text"]="X"
			l1 = Label(top,text="Player 2(O)",height=3,font=('Arial',14,'bold'),bg="white").grid(row=0,column=1)
			board[r][c]="X"
		else:
			button["text"]="O"
			l1 = Label(top,text="Player 1(X)",height=3,font=('tisa',14,'bold'),bg="white").grid(row=0,column=1)
			board[r][c] ="O"

		count = count + 1

		if count >= 5:
			check_winner()
	else :
		messagebox.showerror("Error","This Box is already used")


def check_winner():
	global board,count
	if (board[0][0]==board[0][1]==board[0][2]=="X" or board[1]
		[0]==board[1][1]==board[1][2]=="X" or board[2][0]==board[2]
		[1]==board[2][2]=="X" or board[0][0]==board[1][0]==board[2]
		[0]=="X" or board[0][1]==board[1][1]==board[2][1]=="X" or 
		board[0][2]==board[1][2]==board[2][2]=="X" or
		board[0][0]==board[1][1]==board[2][2]=="X" or board[0]
		[2]==board[1][1]==board[2][0]=="X"):
		display_winner("Player X")
	elif (board[0][0]==board[0][1]==board[0][2]=="O" or board[1]
		  [0]==board[1][1]==board[1][2]=="O" or board[2][0]     
		   ==board[2][1]==board[2][2]=="O" or
		  board[0][0]==board[1][0]==board[2][0]=="O" or board[0]  
		  [1]==board[1][1]==board[2][1]=="O" or board[0]
		  [2]==board[1][2]==board[2][2]=="O" or board[0]
		  [0]==board[1][1]==board[2][2]=="O" or board[0]
		  [2]==board[1][1]==board[2][0]=="O"):
		display_winner("Player O")

	elif ( count == 9 ):
		display_winner("No one ! Its a Draw")

	# destroy_game()

def display_winner(w):
	global top,winner
	winner = Tk()
	winner.title("Winner Window")
	winner.config(bg="black")

	l1 = Label(winner,text="The Winner of the game is :",font=('tisa',15,'bold'),bg="black",fg="white")
	l1.pack()

	l2 = Label(winner,text=w,font=('tisa',15,'bold'),bg="black",fg="white")
	l2.pack()

	b = Button(winner,text = "Okay",command=destroy_game)
	b.pack()

def destroy_game():
	global top,winner
	top.destroy()
	winner.destroy()


def quit():
	global top
	a = messagebox.askquestion("Confirm","Are you sure you want to quit")

	if a == "yes":
		top.destroy()


board_display()

top.mainloop()


