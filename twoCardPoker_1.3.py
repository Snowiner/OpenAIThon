import random
import serve
import serve2

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
		stream = open(self.path,'w')
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

def randomInput(player1, player2, call, cnt):
	print("Random input!")
	if(call>player1.money or player1.money == 0):
		return 0
	else:
		value = random.randrange(0,player1.money)
		print("first value = "+str(value)+" Call = "+str(call))
		player1.save(player2.money,player2.singlePot,cnt,value)
		if(value > player2.money):
			if(call >= player2.money):
				value = call
			else:
				value = player2.money

		if(value<call and value != 0):
			if(random.randrange(0,call)>value):
				return 0
			else:
				return call
		else:
			return value

def aiInput(player1,player2,call,cnt):
	print("OneSon input!")
	if(call>player1.money or player1.money == 0):
		return 0
	else:
		value = int(serve.betting(player1.cards[0],player2.cards[1],player1.money, player2.money, player1.singlePot, player2.singlePot, cnt))
		print("first value = "+str(value)+" call = "+str(call))
		player1.save(player2.money,player2.singlePot,cnt,value)
		if(value > player2.money):
			if(call >= player2.money):
				value = call
			else:
				value = player2.money

		if(value<call and value != 0):
			if(random.randrange(-1,call)>value):
				return 0
			else:
				return call
		elif(value>player1.money):
			return player1.money
		else:
			return value

def aiInput2(player1,player2,call,cnt):
	print("TwoSon input!")
	if(call>player1.money or player1.money == 0):
		return 0
	else:
		value = int(serve2.betting(player1.cards[0],player2.cards[1],player1.money, player2.money, player1.singlePot, player2.singlePot, cnt))
		print("first value = "+str(value)+" call = "+str(call))
		player1.save(player2.money,player2.singlePot,cnt,value)
		if(value > player2.money):
			if(call >= player2.money):
				value = call
			else:
				value = player2.money

		if(value<call and value != 0):
			if(random.randrange(-1,call)>value):
				return 0
			else:
				return call
		elif(value>player1.money):
			return player1.money
		else:
			return value

def userInput(player1,player2, call, cnt):
	if(call>player1.money or player1.money == 0):
		return 0
	else:
		value = input("input value should be over "+call+" lessor than "+player1.money)
		if(value<call and value != 0):
			if(random.randrange(-1,call)>value):
				return 0
			else:
				return call
		elif(value>player1.money):
			return player1.money
		else:
			return value

def cardCollector(player1,player2,deck):
	deck.append(player1.cards.pop())
	deck.append(player1.cards.pop())
	deck.append(player2.cards.pop())
	deck.append(player2.cards.pop())

def printMoney(player1,player2):
	print(str(player1.money)+"/"+str(player2.money) )

def betting(player,enemy,call,cnt):
	if(player.type == 'AI'):
		if(player.name == 'OneSon'):
			return aiInput(player,enemy,call,cnt)
		else:
			return aiInput2(player,enemy,call,cnt)
	elif(player.type == 'user'):
		return userInput(player,enemy,call,cnt)
	else:
		return randomInput(player,enemy,call,cnt)


def flow():
	deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
	pot = 0
	endCall = 1
	call = 0

	player1 = Player('random','OneSon_1.3.csv','OneSon')
	player2 = Player('AI','TwoSon_1.3.csv','TwoSon')
	
	if(random.randrange(1,3)>1):
		turn = player1
	else:
		turn = player2

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
			gold = betting(turn,turnChange(player1,player2,turn),call,cnt)
			print(turn.name+" bets "+str(gold))
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
		return 1
	else:
		print("TwoSon Victories")
		return 2

i = 100000
win1 = 0
win2 = 0
while(i > 0):
	if(flow() == 1):
		win1 +=1
	else:
		win2 +=1
	i = i-1

print(str(win1)+"/"+str(win2))

