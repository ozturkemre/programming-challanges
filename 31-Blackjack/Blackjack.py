import random
cards = {"1": "1" ,"2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7",
         "8": "8", "9": "9", "J": "10", "Q": "10", "K": "10", "A": "11"}


def getcard():
    kart, value = random.choice(list(cards.items()))
    del cards[kart]
    return kart, value


def as_mi(n):
    if n == 11:
        return True
    return False

computer = 0
player = 0
c_as = 0
p_as = 0
c_secim = 1
p_secim = 1

islem = 0

while computer < 21 and player < 21 and islem < 3:
    print("*"*10,"Status","*"*10)
    print("computer's score {} \nplayer's score {} ".format(computer, player))
    if islem == 2:
        if 21 - computer > 6:
            c_secim = 1
            print("computer will take third card.")
        else:
            c_secim = 0
            print("computer wont take third card.")
        try:
            p_secim = int(input("Will you take third card? Type 1 for yes"))
        except:
            p_secim = 0
    if c_secim == 1:
        kart, card = getcard()
        card = int(card)
        print("computer pick up {}".format(kart))
        if as_mi(card):
            c_as += 1
        if card + computer > 21 and c_as > 0:
            computer += 1
            c_as -= 1
        else:
            computer += card
    if p_secim == 1:
        kart, card = getcard()
        card = int(card)
        print("player pick up {}".format(kart))
        if as_mi(card):
            p_as += 1
        if card + player > 21 and p_as > 0:
            player += 1
            p_as -= 1
        else:
            player += card
    islem += 1
print("*"*10, "Scores", "*"*10)
print("computer's score {} \nplayer's score {} ".format(computer, player))
if computer >= 21 or player >= 21:
    if computer == 21:
        if player == 21:
            print("draw")
        else:
            print("computer won")
    elif player == 21:
        print("player won")
    elif computer > 21:
        if player > 21:
            print("draw")
        else:
            print("player won")
    else:
        print("computer won")
elif computer == player:
        print("draw")
else:
    if computer > player:
        print("computer won")
    else:
        print("player won")

