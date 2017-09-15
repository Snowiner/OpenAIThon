global lst
global p1
global p2
global pot
global turnPlayer
global cur_bet

p1 = []
p2 = []
p1.append(100)
p2.append(100)
pot = 0
turnPlayer = p1

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def playerChange():
	global turnPlayer
	if(turnPlayer == p1):
		turnPlayer = p2
	else:
		turnPlayer = p1
	return

def value(player):
	return (player[1]+player[2])%10

def fight():
	global pot
	if(value(p1)>value(p2)):
		print("p1 wins")
		p1[0] += pot
		pot = 0

	else:
		print("p2 wins")
		p2[0] += pot
		pot = 0

	resetGame()
	singleGame()

def surrender():
	global turnPlayer
	global pot
	print("Folded")
	playerChange()
	turnPlayer[0] += pot
	pot = 0

	resetGame()
	singleGame()

def resetGame():
	lst.append(p1.pop())
	lst.append(p1.pop())
	lst.append(p2.pop())
	lst.append(p2.pop())

def bet(player):
	global pot
	global cur_bet
	print(p1)
	print(p2)
	betMoney = int(input("bet money limited by "+str(player[0])+" previous betting was "+str(cur_bet)+"\n"))
	if(betMoney<=player[0] and betMoney>=cur_bet and betMoney>0):
		print("breaking")
		if(betMoney == turnPlayer[0]):
			allIn()
		turnPlayer[0] -= betMoney
		pot += betMoney
		if(cur_bet == betMoney):
			print("CALL")
			fight()
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

def allIn():
	global pot
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
	return deck

def appending():
	global turnPlayer
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

def singleGame():
	deadOneChecking()
	global lst
	global cur_bet
	cur_bet = int(0)
	lst = kiri(lst)

	appending()

	print(value(p1))
	print(value(p2))

	betting()

singleGame()