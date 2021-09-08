
answer = "yes"
while answer == "yes":
    weight = float(input("Please enter your weight in lbs"))
    height = float(input("Please enter your height in inches"))
    BMI = float(weight * (703) / (height ** 2))
    if BMI >= 18.5 and BMI <= 25:
        print("You are at the optimal weight")
    elif BMI < 18.5:
            print("You are under weight")
    elif BMI > 25:
                print('You are over weight')
    answer = input("Would you like to enter your height and weight again? Enter: Yes or No").lower()