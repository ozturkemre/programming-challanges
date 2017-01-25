from collections import Counter

def world(string):
    words = string.split()
    wordCount = Counter(words)
    return wordCount


def numOfWords(x):
    i=0
    for word in x:
        i = i + 1
    return i

entry=input("Enter string: ")

x=world(entry)

a=numOfWords(x)

print("Number of words: ",a)
