import random
import sys
import serve
import serve2

class Game:
    def __init__(self, player1, player2):
        self.pot = 0
        self.lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        self.turnPlayer = player1
        self.nonPlayer = player2
        self.cur_bet = 0
        self.betcnt = 0
        self.available = 0

    def cardAppending(self):
        self.lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        random.shuffle(self.lst)
        self.players[self.turnPlayer].cards[0] = self.lst.pop()
        self.players[(self.turnPlayer+1)%2].cards[0] = self.lst.pop()
        self.players[self.turnPlayer].cards[1] = self.lst.pop()
        self.players[(self.turnPlayer+1)%2].cards[1] = self.lst.pop()

    def enteringFee(self):
        self.players[self.turnPlayer].money = self.players[self.turnPlayer].money - 10
        self.pot += 10
        self.players[(self.turnPlayer+1)%2].money = self.players[(self.turnPlayer+1)%2].money - 10
        self.pot += 10

    def clearBoard(self):
        self.pot = 0
        self.betcnt = 0
        self.players[0].potMoney = 0
        self.players[1].potMoney = 0

    def playerChange(self):
        temp = id(self.turnPlayer)
        self.turnPlayer = id(self.nonPlayer)
        self.nonPlayer = temp
        
    def input_user(self):
        prevalue = input("betting range : " + self.cur_bet + " ~ " + self.players[self.turnPlayer].money)
        value = self.input_validator(prevalue)
        return value

    def input_random(self):
        value = random.randrange(0,self.players[self.turnPlayer].money+1)
        return self.input_validator(value)

    def input_AI(self):
        value = int(serve.betting(self.players[self.turnPlayer].cards[0], self.players[self.turnPlayer].cards[1], self.players[self.turnPlayer].money, self.players[(self.turnPlayer+1)%2].money, self.players[self.turnPlayer].potMoney, self.players[(self.turnPlayer+1)%2].potMoney, self.betcnt))
        return self.input_validator(value)

    def input_validator(self, value):
        if(value > self.players[self.turnPlayer].money):
            return self.players[self.turnPlayer].money
        elif(value == 0):
            return 0
        elif(value < self.cur_bet):
            if(random.randrange(0,self.players[self.turnPlayer].money+1)>value):
                return 0
            else:
                return self.cur_bet
        else:
            return value
    
    def preCheck(self):
        for i in self.players:
            if(i.money == 0):
                self.fight()

        if(self.players[self.turnPlayer].money<self.cur_bet):
            if(self.players[self.turnPlayer].type == 'user'):
                bool = self.all_in_check_user()
            elif(self.players[self.turnPlayer].type == 'AI'):
                bool = self.all_in_check_AI()
            else:
                bool = self.all_in_check_random()

            if(bool == True):
                self.pot += self.players[self.turnPlayer].money
                self.players[self.turnPlayer] = 0
                self.fight()
                return 1
            else:
                self.surrender()
                return 1

    def all_in_check_user(self):
        return input("True or False")

    def all_in_check_random(self):
        return random.choice[True,False]

    def all_in_check_AI(self):
        return serve.betting(self.players[self.turnPlayer].cards[0], self.players[self.turnPlayer].cards[1], self.players[self.turnPlayer].money, self.players[(self.turnPlayer+1)%2].money, self.players[self.turnPlayer].potMoney, self.players[(self.turnPlayer+1)%2].potMoney, self.betcnt)%2


    def betting(self):
        bettingMoney = 0

        if(self.players[self.turnPlayer].type == 'user'):
            bettingMoney = self.input_user()
        elif(self.players[self.turnPlayer].type == 'AI'):
            bettingMoney = self.input_AI()
        else:
            bettingMoney = self.input_random()

        # print(bettingMoney)

        # for i in [self.players[self.turnPlayer].cards[0], self.players[self.turnPlayer].cards[1], self.players[self.turnPlayer].money, self.players[(self.turnPlayer+1)%2].money, self.players[self.turnPlayer].potMoney, self.players[(self.turnPlayer+1)%2].potMoney]:
        #     self.players[self.turnPlayer].data += str(i)
        #     self.players[self.turnPlayer].data += ','
        # self.players[self.turnPlayer].data+= str(self.betcnt)

        self.pot += bettingMoney
        self.players[self.turnPlayer].potMoney += bettingMoney
        if(bettingMoney == 0):
            self.surrender()
        elif(bettingMoney == self.cur_bet):
            self.fight()
        else:
            self.playerChange()

    def fight(self):
        if (self.players[0].value() > self.players[1].value()):
            print("player1 wins")
            players[0].fileStream.write(players[0].data)
            self.players[0].money += self.pot
            self.clearBoard()
            self.available = 1

        elif (self.players[0].value() < self.players[1].value()):
            print("player2 wins")
            players[1].fileStream.write(players[1].data)
            self.players[1].money += self.pot
            self.clearBoard()
            self.available = 1

        else:
            print("draw")

    def surrender(self):
        print("Folded by player"+str(self.turnPlayer+1))
        self.players[(self.turnPlayer+1)%2].money+= self.pot
        self.clearBoard()
        self.available = 1

class Player:
    def __init__(self,type,fileName):
        self.type = type
        print(self.type)
        self.money = 1000
        self.cards = [0,0]
        self.potMoney = 0
        self.fileStream = open(fileName,'a')
        self.data =""

    def value(self):
        return (self.cards[0] + self.cards[1]) % 10

def flow():
    player1 = Player('user','DataOfLastDay1.csv')
    print("player1 set")
    player2 = Player('user','DataOfLastDay2.csv')
    print("player2 set")
    game = Game(player1,player2)
    print("game get")
    game.cardAppending()
    print(player1.cards)
    print(player2.cards)
    print(game.players)
    game.preCheck()

    while(game.available != 1):
        game.betting()

# for i in range(0,100):
flow()

