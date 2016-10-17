print("""Enter 'C' or 'c' for Celsius,
              'K' or 'k' for Kelvin,
              'F' or 'f' for Fahrenheit\n\n""")
converted=0
fr=input("I want converter from: \n")
value1=input("Enter value: \n")
to=input("to: \n")
try:
    value1=float(value1)
    if(fr=='C' or fr=='c'):
        if(to=='F' or to=='f'):
            converted=value1*1,8+32

        elif(to=='K' or to=='k'):
            converted = value1 + 273.15

        else:
            print("you enter different value\n")
            exit()

    elif(fr=='K' or fr=='k'):
        if(to=='C' or to=='c'):
            converted=value1-273.15

        elif(to=='F' or to=='f'):
            converted = (value1 - 273.15) * 1.8 + 32

        else:
            print("you enter different value\n")
            exit()

    elif(fr=='F' or fr=='f'):
        if(to=='C' or to=='c'):
            converted=(value1-32)/1.8

        elif(to=='K' or to=='k'):
            converted = ((f - 32) / 1.8) + 273.15

        else:
            print("you enter different value\n")
            exit()

except ValueError:
    print("That was no valid number.")

print("result = {}".format(converted))
