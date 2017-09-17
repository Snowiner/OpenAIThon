import random

class Player:
	def __init__(self,type,path,name):
		self.type = type
		print(self.type)
		self.path = path
		print(self.path)
		self.cards = []
		self.data = ""
		self.money = 1000
		self.name = name
		self.singlePot = 0

	def dataClear(self):
		self.data = ""

	def write(self):
		stream = open(self.path,'a')
		stream.write(self.data)

	def save(self, foeMoney, foePot, cnt, gold):
		self.data += str(self.cards[0])+","+str(self.cards[1])+","+str(self.money)+","+str(foeMoney)+","+str(self.singlePot)+","+str(foePot)+","+str(cnt)+","+str(gold)+'\n'

def evaluator(cards):
	return (cards[0]+cards[1])%10

def fight(player1, player2, pot):
	if(evaluator(player1.cards)>evaluator(player2.cards)):
		print(player1.name+" wins")
		player1.money += pot
		player1.write()
		player1.dataClear()
		player2.dataClear()
		return 0
	elif(evaluator(player1.cards)<evaluator(player2.cards)):
		print(player2.name+" wins")
		player2.money += pot
		player2.write()
		player2.dataClear()
		player1.dataClear()
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
	if(call>player.money or player.money == 0):
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

def cardCollector(player1,player2,deck):
	deck.append(player1.cards.pop())
	deck.append(player1.cards.pop())
	deck.append(player2.cards.pop())
	deck.append(player2.cards.pop())

def printMoney(player1,player2):
	print(str(player1.money)+"/"+str(player2.money) )

def betting(player,call):
	if(player.type == 'random'):
		return randomInput(player,call)

def flow():
	deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
	pot = 0
	endCall = 1
	call = 0

	player1 = Player('random','OneSon_1.3.csv','OneSon')
	player2 = Player('random','TwoSon_1.3.csv','TwoSon')
	turn = player1

	while(player1.money * player2.money != 0):
		endCall = 1
		call = 0
		pot = 0
		cnt = 0
		player1.singlePot = 0
		player2.singlePot = 0
		appender(deck,player1)
		appender(deck,player2)
		appender(deck,player1)
		appender(deck,player2)

		pot += basicCosting(player1,player2)

		while(endCall):
			gold = betting(turn,call)
			print(turn.name+" bets "+str(gold))
			turn.save(turnChange(player1,player2,turn).money,turnChange(player1,player2,turn).singlePot,cnt,gold)
			cnt = cnt + 1
			turn.singlePot = turn.singlePot+gold

			if( gold == call and call != 0):
				pot += gold
				turn.money -= gold
				endCall = fight(player1,player2, pot)

			elif(gold == 0):
				print(turn.name+" folds")
				endCall = 0
				turn = turnChange(player1,player2,turn)
				turn.write()
				turn.dataClear()
				turn.money += pot
				pot = 0
				turn = turnChange(player1,player2,turn)
				turn.dataClear()

			else:
				turn.money -= gold
				pot += gold
				call = gold

			turn = turnChange(player1,player2,turn)
			print("pot = " + str(pot))
			printMoney(player1,player2)

		print("Single Game Done")
		cardCollector(player1,player2,deck)
		# print(deck)

	if(player1.money != 0):
		print("OneSon Victories")
	else:
		print("TwoSon Victories")

while(1):
	flow()