import random


def create_number():
    number = random.randint(0, 99)
    return number


def make_prediction():
    return input("Guess the number: ")


def check(guess, number):
    if guess > number:
        print("Lower")
    elif guess < number:
        print("Higher")
    return guess == number


def program():
    number = create_number()
    numberoftrials = 0
    while numberoftrials <= 10:
        guess = make_prediction()

        try:
            if check(int(guess), number):
                print("Congratulations you found it. Number of trials: {}".format(numberoftrials))
                break
            else:
                numberoftrials += 1

        except ValueError:
            print("Prediction must be number.")

        except:
            print("Something that should not give an error gave an error.")

    if numberoftrials > 10:

        print("Your predictions were wrong. Number was {}. Sorry :(".format(number))

program()

