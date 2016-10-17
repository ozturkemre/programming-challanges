def fizzbuzz(x):

    if x % 3 == 0 and x % 5 == 0:

        return "Fizz Buzz"

    elif x % 3 == 0:

        return "Fizz"

    elif x % 5 == 0:

        return "Buzz"

    else:

        return str(x)

max=int(input("Maximum number of range : "))

print("\n".join(fizzbuzz(x) for x in range(1,max+1)))