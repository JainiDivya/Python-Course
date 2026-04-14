print("Select your ride")
print("Car")
print("Bike")
choice = input("Enter your choice")

if choice =="car":
    print("What type of car you chose")
    print("1. Sedan")
    print("2. XUV")

    choice2 = input("Enter your choice2:")
    if choice2==1:
        print("you have selected Sedan")
    else:
        print("yyou have selected XUV")
elif choice ==2:
    print("What type of bike")
    print("1. Scooty")
    print("2. Scooter")
    choice3 = input("Enter your choice3:")

    if choice3 ==1:
        print("You have selectedmScooty ")
    else:
        print("You have selected Scooter")

else:
    print("Invalid input")
