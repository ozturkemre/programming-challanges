import random

def doTheMath(x):
    computer=random.randrange(1,6)
    sozluk={"1":"rock",
            "2":"paper",
            "3":"scissors",
            "4":"lizard",
            "5":"spock"}
    print("Player chooses ",sozluk[x])
    print("Computer chooses ",sozluk[str(computer)])

    if ((int(computer)+1)%5 == int(x) ):

        print("Player wins")

    elif ((int(computer)+2)%5 == int(x) ):

        print("Player wins")

    elif (computer == int(x) ):

        print("Draw")

    else:
        print("Computer wins")


x=input("Welcome to the Rock Paper Scissors Lizard Spock\n"
      "Computer waiting to win.\n"
      "Make your choose. Enter : \n"
      "1 for Rock\n"
      "2 for Paper\n"
      "3 for Scissors\n"
      "4 for Lizard\n"
      "5 for Spock:")


doTheMath(x)

