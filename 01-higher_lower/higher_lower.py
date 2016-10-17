import random
number=random.randint(0,99)
estimate=int(input("Guess the number: "))
effort=0
while True:
    effort = effort + 1
    if(estimate>number):
        print("Lower")
    elif(estimate<number):
        print("Higher")
    else:
        break
    estimate = int(input("Guess the number: "))

print("Congratulations you found it. Number of trials:{}".format(effort))