#Caesar cipher

strings="abcdefghijklmnopqrstuwxvyzABCDEFGHIJKLMNOPQRSTUWXVYZ"

def encryption(text,key):
    data=[]
    for i in text:
        if i.strip() and i in strings:
            data.append(strings[(strings.index(i)+key)%52])
        else:
            data.append(i)

    output="".join(data)

    return output


def decryption(text, key):
    data = []
    for i in text:
        if i.strip() and i in strings:
            data.append(strings[(strings.index(i) - key) % 52])
        else:
            data.append(i)

    output = "".join(data)

    return output

try:
    choice=int(input("enter 1 for encryption  "
                     "enter 2 for decryption :"))

    text=input("type text here: ")

    key=int(input("shifting value: "))

    if choice==1:
        result=encryption(text,key)

    elif choice==2:
        result=decryption(text,key)

    else:
        print("enter 1 or 2 !!!")

    print(result)

except TypeError:
    print("enter number !!!")