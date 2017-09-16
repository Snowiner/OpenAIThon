import random

global lst
global p1
global p2
global pot
global turnPlayer
global notTurnPlayer
global cur_bet
<<<<<<< HEAD

global setcost
=======
global priorityP1 = 0
global priorityP2 = 0
global setcost 
>>>>>>> 847b7495d5a937d6ec355c3033b64640386e572a
setcost = 10
p1 = []
p2 = []
p1.append(1000)
p2.append(1000)
pot = 0
turnPlayer = p1
notTurnPlayer = p2

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def p1jokbo(p1):
    p1Card1 = p1[1]
    p1Card2 = p1[2]

    if p1Card1 >= 11:
        p1Card1 = p1[1] % 10
        elif p1Card2 >= 11:
                p1Card2 = p1[2] % 10

    # 삼팔광땡
    if p1Card1 + p1Card2 = 11 and p1Card1 * p1Card2 = 24:
    global priorityP1 = 100
    return

    # 광땡
    if p1Card1 + p1Card2 = 4 and p1Card1 * p1Card2 = 9:
    global priorityP1 = 95
    return

    # 땡
    if p1Card1 == p1Card2:
        global priorityP1 = 90
    return

    # 알리
    if p1Card1 + p1Card2 = 3 and p1Card1 * p1Card2 = 12:
    global priorityP1 = 85
    return

    # 독사
    if p1Card1 + p1Card2 = 5 and p1Card1 * p1Card2 = 4:
    global priorityP1 = 80
    return

    # 구삥
    if p1Card1 + p1Card2 = 10 and p1Card1 * p1Card2 = 9:
    global priorityP1 = 75
    return

    # 장삥
    if p1Card1 + p1Card2 = 11 and p1Card1 * p1Card2 = 10:
    global priorityP1 = 70
    return

    # 세륙
    if p1Card1 + p1Card2 = 10 and p1Card1 * p1Card2 = 24:
    global priorityP1 = 65
    return

        # 갑오
    if p1Card1 + p1Card2 = 9:
    global priorityP1 = 60
    return


def p2Jokbo(p2):
    P2Card1 = p2[1]
    p2Card2 = p2[2]

    if p2[1] >= 11:
        p2Card1 = p2[1] % 10
    elif p2[2] >= 11:
            p2Card2 = p2[2] % 10

    # 삼팔광땡
    if p2Card1 + p2Card2 = 11 and p2Card1 * p2Card2 = 24:
    global priorityP2 = 100
    return

    # 광땡
    if p2Card1 + p2Card2 = 4 and p2Card1 * p2Card2 = 9:
    global priorityP2 = 95
    return

    # 땡
    if p2Card1 == p2Card2:
        global priorityP2 = 90
    return

    # 알리
    if p2Card1 + p2Card2 = 3 and p2Card1 * p2Card2 = 12:
    global priorityP2 = 85
    return

    # 독사
    if p2Card1 + p2Card2 = 5 and p2Card1 * p2Card2 = 4:
    global priorityP2 = 80
    return

    # 구삥
    if p2Card1 + p2Card2 = 10 and p2Card1 * p2Card2 = 9:
    global priorityP2 = 75
    return

    # 장삥
    if p2Card1 + p2Card2 = 11 and p2Card1 * p2Card2 = 10:
    global priorityP2 = 70
    return

    # 세륙
    if p2Card1 + p2Card2 = 10 and p2Card1 * p2Card2 = 24:
    global priorityP2 = 65
    return

    # 갑오
    if p2Card1 + p2Card2 = 9:
    global priorityP2 = 60
    return


def specialJokbo(p1, p2, p1Value, p2Value):
    p1Card1 = p1[1]
    p1Card2 = p1[2]

    p2Card1 = p2[1]
    p2Card2 = p2[2]

    goddeng =
    alri =

    jangddeng =

    kuangddeng =

    # 땡잡이의 경우
    if ((p1Card1 % 10 == 3 and p1Card2 % 10 == 7 and p2Value <= goddeng) or (
                    p1Card1 % 10 == 7 & p1Card2 % 10 == 3 and p2Value <= goddeng)):
        global priorityP1 = 100
        global priorityP2 = 0
        return

    if ((p2Card1 % 10 == 3 and p2Card2 % 10 == 7 and p1Value <= goddeng) or (
                    p2Card1 % 10 == 7 & p2Card2 % 10 == 3 and p1Value <= goddeng)):
        global priorityP1 = 0
        global priorityP2 = 100
        return

    # 멍텅구리 구사
    if ((p1Card1 == 14 and p1Card2 == 19 and p2Value <= jangddeng) and (
                p2Card1 == 14 and p2Card2 == 19 and p1Value <= jangddeng)):
        global priorityP1 = 0
        global priorityP2 = 0
        return

        # 구사
    if ((p1Card1 % 10 == 4 and p1Card2 % 10 == 9 and p2Value <= alri) or (
                    p1Card1 % 10 == 9 & p1Card2 % 10 == 4 and p2Value <= alri)):
        global priorityP1 = 100
        global priorityP2 = 0
        return

    if ((p2Card1 % 10 == 4 and p2Card2 % 10 == 9 and p1Value <= alri) or (
                    p2Card1 % 10 == 9 & p2Card2 % 10 == 4 and p1Value <= alri)):
        global priorityP1 = 0
        global priorityP2 = 100
        return

    # 암행어사
    if (p1Card1 == 14 and p1Card2 == 17 and p2Value == kuangddeng)
        global priorityP1 = 100
        global priorityP2 = 0
        return
    if (p1Card1 == 14 and p1Card2 == 17 and p2Value != kuangddeng)
        global priorityP1 =  # 1끗 가치
        return

    if (p2Card1 == 14 and p2Card2 == 17 and p1Value == kuangddeng)
        global priorityP2 = 100
        global priorityP1 = 0
        return
    if (p2Card1 == 14 and p2Card2 == 17 and p1Value != kuangddeng)
        global priorityP2 =  # 1끗 가치
        return


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
    if (player == turnPlayer)
        p1Jokbo(player)
        else if (player == notTurnPlayer)
            p2Jokbo(player)

    specialJokbo(player, notTurnPlayer, priorityP1, priorityP2)
    # return priorityP1
    return (player[1] + player[2]) % 10


<<<<<<< HEAD
=======
	specialJokbo(player, notTurnPlayer, priorityP1, priorityP2)
	#if (turnplayer == player)
	#	return priorityP1
	#else 
	#	return priorityP2
	return (player[1]+player[2])%10
>>>>>>> 847b7495d5a937d6ec355c3033b64640386e572a
def fight():
    global pot
    if (value(p1) > value(p2)):
        print("p1 wins")
        p1[0] += pot
        pot = 0

<<<<<<< HEAD
    else:
        print("p2 wins")
        p2[0] += pot
        pot = 0

    resetGame()
    singleGame()
=======
	
	else:
		print("p2 wins")
		p2[0] += pot
		pot = 0
>>>>>>> 847b7495d5a937d6ec355c3033b64640386e572a


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
    betMoney = int(input("bet money limited by " + str(player[0]) + " previous betting was " + str(cur_bet) + "\n"))
    if (betMoney <= player[0] and betMoney >= cur_bet and betMoney > 0):
        print("breaking")
        if (notTurnPlayer[0] == 0):
            fight()
        turnPlayer[0] -= betMoney
        pot += betMoney
        if (cur_bet == betMoney):
            print("CALL")
            fight()
        else:
            cur_bet = betMoney
            return
    else:
        if (betMoney == 0):
            surrender()
        else:
            print("invalid input occured, input should be over " + str(cur_bet))
            betMoney = 0
            bet(player)


def allIn():
    global pot
    if (int(input("all in or not\n")) > 0):
        pot += turnPlayer[0]
        turnPlayer[0] = 0
        fight()
    else:
        surrender()


def betting():
    global pot
    global cur_bet

    cur_bet = input("How much you want to bet?")

    # if(cur_bet>=turnPlayer[0]):
    #	allIn()
    # betMoney = bet(turnPlayer)
    # print(pot)
    # if(betMoney == cur_bet):
    #	fight()
    # elif(betMoney == 0):
    #	surrender()
    # else:
    #	print("another betting")
    #	playerChange()
    #	betting()
    return


def kiri(deck):
    random.shuffle(deck)
    return deck


def appending():
    global turnPlayer
    for i in range(4):
        turnPlayer.append(lst.pop())
        playerChange()
    return


def deadOneChecking():
    if (p1[0] < 1):
        print("Player 1 LOSES")
        return exit()
    elif (p2[0] < 1):
        print("Player 2 LOSES")
        return exit()
    else:
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
<<<<<<< HEAD
    global pot

    p1[0] -= setcostcal()
    pot += setcostcal()
    p2[0] -= setcostcal()
    pot += setcostcal()
=======
	global pot
	########################3
	global priorityP1 = 0
	global priorityP2 = 0
	########################3
>>>>>>> 847b7495d5a937d6ec355c3033b64640386e572a


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


singleGame()
