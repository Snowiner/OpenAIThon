global lst
global p1
global p2
global pot
global turnPlayer

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
	if(value(p1)>value(p2)):
		print("p1 wins")
		pot = 0
		p1[0] += pot

	else:
		print("p2 wins")
		pot = 0
		p2[0] += pot

	resetGame()
	singleGame()

def resetGame():
	lst.append(p1.pop())
	lst.append(p1.pop())
	lst.append(p2.pop())
	lst.append(p2.pop())

def bet(player):
	print(p1)
	print(p2)
	betMoney = int(input("bet money under"+str(player[0])))
	if(betMoney<player[0] and betMoney>1):
		return betMoney
	else:
		bet(player)

def betting(prevBet):
	global pot
	betMoney = bet(turnPlayer)
	print(type(betMoney))
	print(betMoney)
	if(type(betMoney) == int):
		turnPlayer[0] -= betMoney
		pot += betMoney

	if(turnPlayer[0] == 0 and prevBet != 0):
		fight()
	elif(betMoney == prevBet):
		fight()
	else:
		playerChange()
		betting(betMoney)
	return

def kiri(deck):
	return deck

def appending():
	global turnPlayer
	for i in range(4):
		turnPlayer.append(lst.pop())
		playerChange()
	return

def singleGame():
	global lst

	lst = kiri(lst)

	appending()

	print(p1)
	print(p2)

	print(value(p1))
	print(value(p2))

	betting(-1)

singleGame()