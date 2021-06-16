import random

def coin_unbiased():
	print("----------------------------------------------------------------------------------------------------")
	print("Coin is Flipping")
	print("The value of the coin is :")
	print("----------------------------------------------------------------------------------------------------")

	s = ('HEAD','TAIL')
	print(random.choice(s))

	return 0

def coin_biased():
	print("----------------------------------------------------------------------------------------------------")
	print("Coin is Flipping")
	print("The value of the coin is :")
	print("----------------------------------------------------------------------------------------------------")

	s = ('HEAD','HEAD','HEAD','TAIL','TAIL')
	print(random.choice(s))

	return 0


def dice_unbiased(min,max):
	print("----------------------------------------------------------------------------------------------------")
	print("Dice is Rolling")
	print("The value of the dice is :")
	print("----------------------------------------------------------------------------------------------------")

	a = random.randint(min,max)
	print(a)

	return 0


def dice_biased(min,max):
	print("----------------------------------------------------------------------------------------------------")
	print("Dice is Rolling")
	print("The value of the dice is :")
	print("----------------------------------------------------------------------------------------------------")

	s = (1,1,1,2,3,3,3,3,3,4,4,5,5,5,6,6,6,6,6)
	a = random.choice(s)
	print(a)

	return 0

min=1
max=6

roll = "y"

c = input("Do you want to throw a dice or flip a coin (d/c)")

if(c=="d"):
	dice = input("Do you want a biased dice (y/n)")
	if(dice=="y") :
		while(roll == "y"):
			dice_biased(min,max)
			roll = input("Do you want to roll again witht same dice(y/n)")

			if(roll == "n"):
				print("Thank you for playing")

	else :
		while(roll == "y"):
			dice_unbiased(min,max)
			roll = input("Do you want to roll again (y/n)")

			if(roll == "n"):
				print("Thank you for playing")


if(c=="c"):
	coin = input("Do you want a biased coin (y/n)")
	if(coin=="y") :
		while(roll == "y"):
			coin_biased()
			roll = input("Do you want to flip again witht same dice(y/n)")

			if(roll == "n"):
				print("Thank you for playing")

	else :
		while(roll == "y"):
			coin_unbiased()
			roll = input("Do you want to flip again (y/n)")

			if(roll == "n"):
				print("Thank you for playing")