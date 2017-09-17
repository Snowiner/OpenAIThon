import random

class Player:
	def __init__(self,type,path):
		self.type = type
		print(self.type)
		self.path = path
		print(self.path)
		self.cards = []
		self.data = ""
		self.money = 1000

	def dataClear(self):
		self.data = ""

def evaluator(cards):
	return (cards[0]+cards[1])%10

def fight(player1, player2, pot):
	if(evaluator(player1.cards)>evaluator(player2.cards)):
		print("player1 wins")
		player1.money += pot
		return 0
	elif(evaluator(player1.cards)<evaluator(player2.cards)):
		print("player2 wins")
		player2.money += pot
		return 0
	else:
		print("draw game")
		return 1

def turnChange(player1,player2, turn):
	if(turn == player1):
		return player2
	else:
		return player1

def appender(deck, player):
	random.shuffle(deck)
	player.cards.append(deck.pop())

def basicCosting(player1, player2):
	cost = 10
	pot = 0

	if(player1.money < cost):
		cost = player1.money
	if(player2.money < cost):
		cost = player2.money

	player1.money -= cost
	pot += cost
	player2.money -= cost
	pot += cost

	return pot

def randomInput(player,call):
	if(call>player.money):
		return 0
	else:
		value = random.randrange(0,player.money)
		if(value<call and value != 0):
			if(random.randrange(-1,call)>value):
				return 0
			else:
				return call
		else:
			return value

def printMoney(player1,player2):
	print(str(player1.money)+str(player2.money) )

def betting(player,call):
	if(player.type == 'random'):
		return randomInput(player,call)

def flow():
	deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
	pot = 0
	endCall = 1
	call = 0

	player1 = Player('random','p1Data_1.3.csv')
	player2 = Player('random','p2Data_1.3.csv')
	turn = player1


	appender(deck,player1)
	appender(deck,player2)
	appender(deck,player1)
	appender(deck,player2)

	pot += basicCosting(player1,player2)

	while(endCall):
		gold = betting(turn,call)
		if( gold == call and call != 0):
			pot += gold
			turn.money -= gold
			endCall = fight(player1,player2, pot)

		elif(betting == 0):
			endCall = 0
			turn = turnChange(player1,player2,turn)
			turn.money += pot
			pot = 0

		else:
			turn.money -= gold
			pot += gold
			call = gold

		print("pot = " + str(pot))

flow()