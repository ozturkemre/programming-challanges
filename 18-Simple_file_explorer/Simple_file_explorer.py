#! usr/bin
import os
now="/home"
os.chdir(now)
while True:
    print("\nCurrent directory : ")
    os.system("pwd")
    print("\nDirectories: ")
    os.system("ls -d */")
    print("\nFiles: ")
    os.system("ls -p | grep -v /")
    target=input("\nchange directory to : \n"
              "2 to exit: \n")
    if(target=="2"):
        print("Goodbye")
        exit()
    else:
        try:
            now = now + "/" + target
            os.chdir(now)
        except:
            print("Enter valid directory \n")
