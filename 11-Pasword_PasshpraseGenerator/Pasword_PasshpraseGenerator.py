import os
import random

charSet={"digits":"0123456789",
         "letters":"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
         "others":"!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"}

password=[]

while(len(password)<25):
    key = random.choice(random.choice(list(charSet.values())))
    #choice from charSet's key that we have already choiced from values
    password.append(key)

print("Your password is:  ",*password)