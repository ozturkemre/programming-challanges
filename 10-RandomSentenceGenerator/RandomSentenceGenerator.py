import random

nouns=("John","Plato","Sharon","Grandfather","Dog","Cat","Money","Horse","Tree")
verbs=("runs","hear","know","believe","is","call","drives","jumps")
adv=("financially","willfully","abruptly","endlessly","firmly","delightfully","quickly","lightly","eternally")
adj=("aggressive","famous","restless","agoraphobic","fearless","rich","ambidextrous","fertile","righteous")

all=[nouns,verbs,adv,adj]

i=0
result=[]
while i<4:

    result.append(random.choice(all[i]))
    #choice of one of all elements and append to list.
    i=i+1

print(*result)
#print result list's elements.