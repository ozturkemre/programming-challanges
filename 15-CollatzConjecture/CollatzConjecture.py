try:
    entry=int(input("Enter the number: \n"))
    i=entry
    x=entry
    #biggest number
    status=[]

    while(i!=1):
        #end
        status.append(i)
        if i%2==0:
            i=int(i/2)

        else:
            i=3*i+1

        if(i>x):
            x=i
    status.append(i)
    print(*status)
    print("The biggest number: {}".format(x))
except ValueError:
    print("I said number!!!")