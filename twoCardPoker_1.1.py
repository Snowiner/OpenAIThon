import random
import sys
import serve
import serve2

global lst
global p1
global p2
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
global p1stack
global p2stack
global betcnt
global setcost
global showJokbo
global showJokbo2


def ValueReset():
    global lst
    global p1
    global p2
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
    global p1stack
    global p2stack
    global betcnt
    global setcost
    global showJokbo
    global showJokbo2
    data = ""
    data1 = ""
    data2 = ""
    p1stack = 0
    p2stack = 0
    betcnt = 0
    setcost = 10
    showJokbo = ""
    showJokbo2 = ""
    p1 = []
    p2 = []
    p1.append(1000)
    p2.append(1000)
    pot = 0
    turnPlayer = p1
    notTurnPlayer = p2
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def Set(firstCard, secondCard):
    Jokbo = {'38GwangDDeng': 100,
             'GwangDDeng': 95,
             'DDeng': 90,
             'ArLi': 85,
             'Doksa': 80,
             '9BBing': 75,
             'JangBBing': 70,
             'Sseryuk': 65,
             'Gab5': 60
             }


# Jokbo.get('38GwangDDeng')

def playerChange():
    global turnPlayer
    if (turnPlayer == p1):
        turnPlayer = p2
        notTurnPlayer = p1
    else:
        turnPlayer = p1
        notTurnPlayer = p2
    return


def value(player):
    return (player[1] + player[2]) % 10


def fight():
    global pot
    global p1stack
    global p2stack
    global showJokbo
    # showJokbo = Jokbo(p1[1],p1[2])
    # showJokbo2 = Jokbo(p2[1],p2[2])

    global f1
    global data1
    global f2
    global data2

    if (value(p1) > value(p2)):
        print("p1 wins")
        f1.write(data1)
        data1 = ""
        data2 = ""
        p1[0] += pot
        pot = 0
        p1stack = 0
        p2stack = 0
    elif (value(p2) > value(p1)):
        print("p2 wins")
        f2.write(data2)
        data1 = ""
        data2 = ""
        p2[0] += pot
        pot = 0
        p1stack = 0
        p2stack = 0

    return


def surrender():
    global turnPlayer
    global pot
    global p1stack
    global p2stack
    global betcnt
    global data1
    global data2

    print("Folded")

    if(turnPlayer == p1):
        f2.write(data2)
    else:
        f1.write(data1)

    data1=""
    data2=""
    notTurnPlayer[0] += pot
    pot = 0

    p1stack = 0
    p2stack = 0
    betcnt = 0

    return


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
    print(sys.argv)
    print(id(turnPlayer))
    if (sys.argv[1] == 'test'):
        global betcnt, p1stack, p2stack, betMoney

        if (turnPlayer == p1):
            print(p1)
            global data1
            # data1 = str(id(p1))+","
            data1 = str(p1[1]) + ","
            data1 += str(p1[2]) + ","
            data1 += str(p1[0]) + ","
            data1 += str(p2[0]) + ","
            data1 += str(p1stack) + ","
            data1 += str(p2stack) + ","
            data1 += str(betcnt) + ","

            betMoney = int(serve.betting(p1[1], p1[2], p1[0], p2[0], p1stack, p2stack, betcnt))
            print(betMoney)
            if betMoney < cur_bet:
                if random.randrange(cur_bet) > betMoney:
                    surrender()
                    return
                else:
                    betMoney = cur_bet
                    allIn()
                    return
            elif betMoney > turnPlayer[0]:
                betMoney = turnPlayer[0]
            # betMoney = random.randrange(cur_bet, turnPlayer[0] + 1)

            p1stack += betMoney
            betcnt = betcnt + 1
            data1 += str(betMoney) + "\n"
        else:
            global data2
            # data2 = str(id(p2))+","
            data2 = str(p2[1]) + ","
            data2 += str(p2[2]) + ","
            data2 += str(p2[0]) + ","
            data2 += str(p1[0]) + ","
            data2 += str(p2stack) + ","
            data2 += str(p1stack) + ","
            data2 += str(betcnt) + ","

            betMoney = int(serve2.betting(p2[1], p2[2], p2[0], p1[0], p2stack, p1stack, betcnt))
            if betMoney < cur_bet:
                if random.randrange(cur_bet) > betMoney:
                    betMoney = 0
                else:
                    betMoney = cur_bet
            elif betMoney > turnPlayer[0]:
                betMoney = turnPlayer[0]
            # betMoney = random.randrange(cur_bet, turnPlayer[0] + 1)

            p2stack += betMoney
            betcnt = betcnt + 1
            data2 += str(betMoney) + "\n"

    else:
        betMoney = int(input("bet money limited by " + str(player[0]) + " previous betting was " + str(cur_bet) + "\n"))

    if (betMoney <= player[0] and betMoney >= cur_bet and betMoney > 0):
        print("breaking")
        if (notTurnPlayer[0] == 0):
            fight()
            return
        turnPlayer[0] -= betMoney
        pot += betMoney
        if (cur_bet == betMoney):
            print("CALL!")
            fight()
            return
        else:
            cur_bet = betMoney
            playerChange()
            return
    else:
        if (betMoney == 0):
            surrender()
        else:
            print(betMoney)
            print("invalid input occured, input should be over " + str(cur_bet))
            betMoney = 0
            bet(player)


def allIn():
    global pot
    global betcnt, p1stack, p2stack, turnPlayer
    print("allin status")
    if (sys.argv[1] == 'test'):
        if (random.choice([True, False])):
            if (turnPlayer == p1):

                # data = str(id(p1))+","
                data = str(p1[1]) + ","
                data += str(p1[2]) + ","
                data += str(p1[0]) + ","
                data += str(p2[0]) + ","
                data += str(p1stack) + ","
                data += str(p2stack) + ","
                data += str(betcnt) + ","
                data += str(turnPlayer[0]) + "\n"
                p1stack += turnPlayer[0]
            else:

                # data = str(id(p2))+","
                data = str(p2[1]) + ","
                data += str(p2[2]) + ","
                data += str(p2[0]) + ","
                data += str(p1[0]) + ","
                data += str(p2stack) + ","
                data += str(p1stack) + ","
                data += str(betcnt) + ","
                data += str(turnPlayer[0]) + "\n"
                p2stack += turnPlayer[0]

            pot += turnPlayer[0]
            turnPlayer[0] = 0
            betcnt = betcnt + 1
            fight()
            return
        else:
            surrender()
    else:
        if (int(input("all in or not\n")) > 0):
            pot += turnPlayer[0]
            turnPlayer[0] = 0
            fight()
        else:
            surrender()


def betting():
    global pot
    global cur_bet
    
    if (cur_bet >= turnPlayer[0]):
        allIn()
        return
    betMoney = bet(turnPlayer)
    print(pot)
    if (betMoney == cur_bet):
        fight()
    elif (betMoney == 0):
        surrender()
    else:
        print("another betting")
        if(turnPlayer[0] == 0):
            surrender()
        playerChange()
        betting()
    return


def kiri(deck):
    random.shuffle(deck)
    return deck


def appending():
    global turnPlayer
    for i in range(4):
        turnPlayer.append(lst.pop())
        playerChange()

    print(turnPlayer)
    return


def min():
    if (p1[0] > p2[0]):
        return p2[0]
    else:
        return p1[0]


def setcostcal():
    global setcost
    if (min() < setcost):
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
    if (p1[0] < 1):
        print("Player 1 LOSES")
        return
    elif (p2[0] < 1):
        print("Player 2 LOSES")
        return

    global lst
    global cur_bet
    gamestart()

    cur_bet = int(0)
    lst = kiri(lst)

    appending()

    print(value(p1))
    print(value(p2))

    betting()


if (sys.argv[1] == 'test'):
    # global f
    global f1
    global f2
    # f = open('testdata.txt','a')
    f1 = open('dataset_new.csv', 'a')
    f2 = open('dataset2_new.csv', 'a')

while (1):
    ValueReset()
    singleGame()
    print("Game reset")
    resetGame()
