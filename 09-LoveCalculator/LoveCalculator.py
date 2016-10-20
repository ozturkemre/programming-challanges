import random

i=random.randint(1,20)

myName=input("Your name ?: \n")

hName=input("Her(his) name ? :\n")

result=abs(100-(len(myName)*len(hName))-i)

print("Chance of finding true love together: {}".format(result))