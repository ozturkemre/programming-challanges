#! usr/bin
import os
now=os.getcwd()
os.chdir(now)
while True:
    print("\nCurrent directory : ")
    print(now)
    print("\nList directory: ")
    print(os.listdir(os.getcwd()))
    target=input("\nchange directory to : \n")
    try:
        s.chdir(now)
        now = now + "/" + target
    except:
        os.chdir(target)
        now=target
