import random
import sys

global lst
global p1
global p2
global Secondp1
global Secondp2
global pot
global turnPlayer
global notTurnPlayer
global cur_bet
global f
global f1
global f2
global data
global data1
global data2
data=""
data1=""
data2=""
global p1stack
global p2stack
global Secondp1stack
global Secondp2stack
p1stack = 0
p2stack = 0
Secondp1stack = 0
Secondp2stack = 0
global betcnt
betcnt = 0
global setcost
setcost = 10
global IsCall
IsCall = 0
global showJokbo
global showJokbo2
showJokbo = ""
showJokbo2 = ""
p1 = []
p2 = []
Secondp1 = []
Secondp2 = []
p1.append(1000)
p2.append(1000)
pot = 0
turnPlayer = p1
notTurnPlayer = p2

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


def Jokbo(firstCard,secondCard):
	if(firstCard + secondCard = 4 || firstCard * secondCard = 9)
		
	
        
def playerChange():
	global turnPlayer
	if(turnPlayer == p1):
		turnPlayer = p2
		notTurnPlayer = p1
	else:
		turnPlayer = p1
		notTurnPlayer = p2
	return

def value(player):
	return (player[1]+player[2])%10

def fight():
	global pot
	global p1stack
	global p2stack
<<<<<<< HEAD
	global IsCall
	global showJokbo
	
	if(IsCall = 1):
		showJokbo = Jokbo(p1,Secondp1)
		showJokbo2 = Jokbo(p2, Secondp2)
		
		
			if(value(p1)>value(p2)):
				print("p1 wins")
				p1[0] += pot
				pot = 0
				p1stack = 0
				p2stack = 0

			else:
				print("p2 wins")
				p2[0] += pot
				pot = 0
				p1stack = 0
				p2stack = 0
=======
	global f1
	global data1
	global f2
	global data2
	if(value(p1)>value(p2)):

		print("p1 wins")
		f1.write(data1)
		data1 = ""
		data2 = ""
		p1[0] += pot
		pot = 0
		p1stack = 0
		p2stack = 0

	elif(value(p2)>value(p1)):
		
		print("p2 wins")
		f2.write(data2)
		data1=""
		data2=""
		p2[0] += pot
		pot = 0
		p1stack = 0
		p2stack = 0
>>>>>>> c7e891c444d938ca8e5fb53b4312931c4e06eee5

	resetGame()
	singleGame()

def surrender():
	global turnPlayer
	global pot
	global p1stack
	global p2stack
	print("Folded")
	playerChange()
	turnPlayer[0] += pot
	pot = 0
	p1stack = 0
	p2stack = 0

	resetGame()
	singleGame()

def resetGame():
	lst.append(p1.pop())
	lst.append(p1.pop())
	lst.append(p2.pop())
	lst.append(p2.pop())
	lst.append(Secondp1.pop())
	lst.append(Secondp1.pop())
	lst.append(Secondp2.pop())
	lst.append(Secondp2.pop())	

def bet(player):
	global pot
	global cur_bet
	print(p1)
	print(p2)
	print(sys.argv)
	print(id(turnPlayer))
	if(sys.argv[1] == 'test'):
		global betcnt,p1stack,p2stack,betMoney
		
		if(turnPlayer == p1):
<<<<<<< HEAD
			# data = str(id(p1))+","
			data = str(p1[1])+","
			data += str(p1[2])+","
			data += str(p1[0])+","
			data += str(p2[0])+","
			data += str(p1stack)+","
			data += str(p2stack)+","
			data += str(betcnt)+","
=======
			global data1
			# data1 = str(id(p1))+","
			data1 = str(p1[1])+","
			data1 += str(p1[2])+","
			data1 += str(p1[0])+","
			data1 += str(p2[0])+","
			data1 += str(p1stack)+","
			data1 += str(p2stack)+","
			data1 += str(betcnt)+","
>>>>>>> c7e891c444d938ca8e5fb53b4312931c4e06eee5
			betMoney = random.randrange(cur_bet,turnPlayer[0])
			p1stack += betMoney
			betcnt = betcnt + 1
			data1 += str(betMoney)+"\n"
		else:
<<<<<<< HEAD
			# data = str(id(p2))+","
			data = str(p2[1])+","
			data += str(p2[2])+","
			data += str(p2[0])+","
			data += str(p1[0])+","
			data += str(p2stack)+","
			data += str(p1stack)+","
			data += str(betcnt)+","
=======
			global data2
			# data2 = str(id(p2))+","
			data2 = str(p2[1])+","
			data2 += str(p2[2])+","
			data2 += str(p2[0])+","
			data2 += str(p1[0])+","
			data2 += str(p2stack)+","
			data2 += str(p1stack)+","
			data2 += str(betcnt)+","
>>>>>>> c7e891c444d938ca8e5fb53b4312931c4e06eee5
			betMoney = random.randrange(cur_bet,turnPlayer[0])
			p2stack += betMoney

			betcnt = betcnt + 1
			data2 += str(betMoney)+"\n"
		
	else:
		betMoney = int(input("bet money limited by "+str(player[0])+" previous betting was "+str(cur_bet)+"\n"))
	if(betMoney<=player[0] and betMoney>=cur_bet and betMoney>0):
		print("breaking")
		if(notTurnPlayer[0] == 0):
			fight()
		turnPlayer[0] -= betMoney
		pot += betMoney
		if(cur_bet == betMoney):
			# Call()
			print("CALL!")
		else:
			cur_bet = betMoney
			return
	else:
		if(betMoney == 0):
			surrender()
		else:
			print("invalid input occured, input should be over "+str(cur_bet))
			betMoney = 0
			bet(player)
<<<<<<< HEAD
def Call():
        global IsCall
        
		print("Do you want to Call? Y or N")
		if(sys.argv[1] == Y)
			IsCall = 1										# Player has called
			fight()
			else
				fight()
=======
# def Call():
#     global IsCall
    
# 	print("Do you want to Call? Y or N")
# 	if(sys.argv[1] == Y):
# 		IsCall = 1										# Player has called
# 	else:
# 		fight()
>>>>>>> c7e891c444d938ca8e5fb53b4312931c4e06eee5
        
def allIn():
	global pot
	global betcnt,p1stack,p2stack,turnPlayer
	if(sys.argv[1] == 'test'):
		if(random.choice([True,False])):
			if(turnPlayer == p1):
<<<<<<< HEAD
				
				# data = str(id(p1))+","
				data = str(p1[1])+","
				data += str(p1[2])+","
				data += str(p1[0])+","
				data += str(p2[0])+","
				data += str(p1stack)+","
				data += str(p2stack)+","
				data += str(betcnt)+","
				data += str(turnPlayer[0])+"\n"
				p1stack += turnPlayer[0]
			else:
				
				# data = str(id(p2))+","
				data = str(p2[1])+","
				data += str(p2[2])+","
				data += str(p2[0])+","
				data += str(p1[0])+","
				data += str(p2stack)+","
				data += str(p1stack)+","
				data += str(betcnt)+","
				data += str(turnPlayer[0])+"\n"
=======
				global data1
				# data1 = str(id(p1))+","
				data1 += str(p1[1])+","
				data1 += str(p1[2])+","
				data1 += str(p1[0])+","
				data1 += str(p2[0])+","
				data1 += str(p1stack)+","
				data1 += str(p2stack)+","
				data1 += str(betcnt)+","
				data1 += str(turnPlayer[0])+"\n"
				p1stack += turnPlayer[0]
			else:
				global data2
				# data2 = str(id(p2))+","
				data2 += str(p2[1])+","
				data2 += str(p2[2])+","
				data2 += str(p2[0])+","
				data2 += str(p1[0])+","
				data2 += str(p2stack)+","
				data2 += str(p1stack)+","
				data2 += str(betcnt)+","
				data2 += str(turnPlayer[0])+"\n"
>>>>>>> c7e891c444d938ca8e5fb53b4312931c4e06eee5
				p2stack += turnPlayer[0]
			
			pot += turnPlayer[0]
			turnPlayer[0] = 0
			betcnt = betcnt+1
			fight()
		else:
			surrender()
	if(int(input("all in or not\n"))>0):
		pot += turnPlayer[0]
		turnPlayer[0]=0
		fight()
	else:
		surrender()

def betting():
	global pot
	global cur_bet

	if(cur_bet>=turnPlayer[0]):
		allIn()
	betMoney = bet(turnPlayer)
	print(pot)
	if(betMoney == cur_bet):
		fight()
	elif(betMoney == 0):
		surrender()
	else:
		print("another betting")
		playerChange()
		betting()
	return

def kiri(deck):
	random.shuffle(deck)
	return deck

def appending():
	global IsCall
	global turnPlayer
	global Secondp1
	if(IsCall == 1)												# if player has called draw one more card
		for i in range(4):
			Secondp1.append(lst.pop())
			playerChange()
			return
			else
				for i in range(4):
					turnPlayer.append(lst.pop())
					playerChange()
				return

def deadOneChecking():
	if(p1[0]<1):
		print("Player 1 LOSES")
		return exit()
	elif(p2[0]<1):
		print("Player 2 LOSES")
		return exit()
	else:
		return

def min():
	if(p1[0]>p2[0]):
		return p2[0]
	else:
		return p1[0]

def setcostcal():
	global setcost
	if(min()<setcost):
		return min()
	else:
		return setcost

def gamestart():
	global pot

	p1[0] -= setcostcal()
	pot += setcostcal()
	p2[0] -= setcostcal()
	pot += setcostcal()

def singleGame():
	deadOneChecking()
	global lst
	global cur_bet
	gamestart()

	cur_bet = int(0)
	lst = kiri(lst)

	appending()

	print(value(p1))
	print(value(p2))

	betting()

if(sys.argv[1] == 'test'):
	global f
	global f1
	global f2
	f = open('testdata.txt','a')
	f1 = open('testdata1.txt','a')
	f2 = open('testdata2.txt','a')
singleGame()
