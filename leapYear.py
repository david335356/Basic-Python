
year = 1
answer = "yes"

while answer == "yes":
    year = int(input("Enter a year Sir/Ma'am: "))
    if (year % 100) == 0 and (year % 400) == 0:
        print('The year,', year, "is considered a leap year which contains 29 days in February")
        answer = input("Would you like to enter another year?").lower()
    elif (year % 4) == 0:
        print('The year ', year, 'Is considered a leap year which contains 29 days in Feb~~!!!')
        answer = input("Would you like to enter another year?").lower()
    else:
        print("The year", year, "has 28 days in February which isn't considered a leap year")
        answer = input("Would you like to enter another year?").lower()