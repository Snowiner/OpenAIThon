def value(player):
	return (player[0]+player[1])%10

def fight(p1,p2,pot,p1m,p2m):
	if(value(p1)>value(p2)):
		print("p1 wins")
		p1m += pot
		pot = 0
	else:
		print("p2 wins")
		p2m += pot
		pot = 0

def resetGame(deck,p1,p2):
	deck.append(p1.pop())
	deck.append(p1.pop())
	deck.append(p2.pop())
	deck.append(p2.pop())

def betting()


list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

p1 = []
p2 = []

p1m = 100
p2m = 100
pot = 0

p1.append(list.pop())
p2.append(list.pop())
p1.append(list.pop())
p2.append(list.pop())

print(p1, p1m)
print(p2, p2m)

print(value(p1))
print(value(p2))

fight(p1,p2,pot,p1m,p2m)
resetGame(list,p1,p2)