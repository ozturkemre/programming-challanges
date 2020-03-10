from datetime import datetime, date


def calculate(birth):
    now = datetime.now()
    difference = (now - birth)
    difference_in_secs = difference.days * 24 * 60 * 60 + difference.seconds
    return difference_in_secs


print("Enter your date of birth (dd mm yyyy) format :")

date_of_birth = datetime.strptime(input(" "), "%d %m %Y")

print(calculate(date_of_birth))
