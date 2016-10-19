import random
#all mode possibilities
modes = ['''

   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']

words=["apple","apricot","avocado","banana","bilberry","blackberry","blackcurrant","blueberry","boysenberry",
       "currant","cherry","cherimoya","cloudberry","coconut","cranberry","damson","date","dragonfruit","durian",
       "elderberry","feijoa","fig","gooseberry","grape","grapefruit","guava","honeyberry","huckleberry","jabuticaba",
       "jackfruit","jambul","jujube","kiwifruit","kumquat","lemon","lime","loquat","longan","lychee","mango",
       "marionberry","melon","mulberry","nectarine","nance","olive","orange","papaya","passionfruit","peach",
       "pear","persimmon","physalis","plantain","plum","pineapple","plumcot","pomegranate","pomelo","quince",
       "raspberry","rambutan","redcurrant","salak","satsuma","strawberry","tamarillo","tamarind","tomato","yuzu"]


word=random.choice(words)
#getting random word

current=0

temp="- "*(len(word)-1)

temp=temp.split(' ')

print(modes[current])

#print(word)

while current != 6:
#while our man still alive

    print(temp)
    if "-" in temp:

        entry=input("Enter letter: \n")
        #user enter letter
        entry=entry.lower()
        #convert entry to lower one.

        if entry in word:

            x=0
            for i in word:
            #to find which character(s) similar

                if i==entry:
                    temp[x]=i
                    #changed "-" with entry

                x=x+1
        else:
        #run when guess was wrong.

            current=current+1
            print(modes[current])
            #show our man's mode

    else:
        #if "-" not in temp. that mean no more "-" left.
        print("You won")
        exit()

print("You lose. word was {}".format(word))