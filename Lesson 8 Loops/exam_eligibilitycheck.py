medical_cause = input("Do you have medical cause-Yes or No")
atten = input("Enter your attendance")
if medical_cause == "Yes":
    print("You are allowed for exam")
else:
    print("You are not allowed for exam")
    if atten >= 75:
        print("You are allowed for exam")
    else:
        print("You are not allowed")