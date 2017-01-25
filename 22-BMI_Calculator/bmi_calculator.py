#formula for The Body Mass Index (BMI)
#for kg and m:
#   bmi = x kg/(y m * y m)

def get_value(): #getting value
    try:
        value=int(input("Enter the value: \n"))
        return value
    except:
        print("Entered something not type of int")
        exit()

def convert_to_kg(value): #convet lb to kg
    value=value*0.45359237
    return value

def convert_to_cm(value): #convert inch to cm
    value=value*2.54
    return value

def choose_kg_or_lb(): #choose kg or lb
    x=input("enter 1 for kg, enter 2 for lb (default kg) :\n")
    return x

def kg_or_lb(x): #if choosed lb ,convert kg and return.
    value=get_value()
    if(x==2):
        kg_value=convert_to_kg(value)
        return kg_value
    else:
        return value

def choose_cm_or_inch(): #choose cm or inch
    x=input("enter 1 for cm, enter 2 for inch (default kg) :\n")
    return x

def cm_or_inch(x): #if choosed inch ,convert cm and return.
    value=get_value()
    if(x==2):
        cm_value=convert_to_cm(value)
        return cm_value
    else:
        return value

def to_do_math(a,b): #calculate bmi
    i=a/(b*b/10**4)
    return i

def print_result(kway,cway,result): #print result
    print("\nkg : {} cm : {} BMI : {}\n".format(kway, cway, result))
    get_table(result)

def get_table(res): #print table result
    if(res<18.5):
        print("less than 18.5: underweight\n")
        print("-"*80)
        print("\nBMI of less than 18.5kg/m2\n"
              "A BMI of less than 18.5 indicates that you are underweight, \n"
              "so you may need to put on some weight.\n"
              "You are recommended to ask your Doctor or a dietician for advice.\n")
        print("-"*80)
    elif(res<25):
        print("18.5 - 25: normal weight\n")
        print("-"*80)
        print("\nBMI of 18.5 - 25kg/m2\n"
              "A BMI of 18.5 - 25 indicates that you are at a healthy weight for your height.\n"
              " By maintaining a healthy weight, you lower your risk of developing serious health problems.\n")
        print("-"*80)
    elif(res<30):
        print("25 - 30: overweight\n")
        print("-"*80)
        print("\nBMI of 25 - 30kg/m2\n"
              "A BMI of 25 - 30 indicates that you are slightly overweight.\n"
              "You may be advised to lose some weight for health reasons.\n"
              "You are recommended to talk to your Doctor or a dietician for advice.\n")
        print("-" * 80)
    else:
        print("over 30: heavily overweight")
        print("-" * 80)
        print("\nBMI of over 30kg/m2\n"
              "A BMI of over 30 indicates that you are heavily overweight.\n"
              "Your health may be at risk if you do not lose weight.\n"
              "You are recommended to talk to your Doctor or a dietician for advice.\n")
        print("-" * 80)


kol=choose_kg_or_lb() #kg or lb
kway=kg_or_lb(kol) #converted kg

cori=choose_cm_or_inch() #cm or inch
cway=cm_or_inch(cori) #converted cm

result=round(to_do_math(kway,cway),2) #getting result
print_result(kway,cway,result) #print result
