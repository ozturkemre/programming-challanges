#! usr/bin
import os
now=os.getcwd()
os.chdir(now)
while True:
    print("Working directory : ")
    print(os.getcwd())
    print("\nList directory: ")
    space = 0
    for i in os.listdir(os.curdir):
        print("-"*space,">",i)
        space += 1
    target=input("\nchange directory to : \n")

    if os.path.exists(target):
        if os.path.isdir(target):
            os.chdir(target)
            now=os.getcwd()
        else:
            temp = os.path.join(now,target)
            if os.path.isfile(temp):
                print("Can't change directory to file")
            else:
                if os.path.exists(temp):
                    now = temp
                    os.chdir(now)
                else:
                    print("No such file or directory\n")
