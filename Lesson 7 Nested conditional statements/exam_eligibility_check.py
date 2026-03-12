Medical_cause = input("Enter If you have medical cause i.e yes or no:")

if Medical_cause == "Yes":
    print("You are allowed for exam")
else:
  atten = int(input("Enter the attendance of the student"))
  
if atten>=75:
     print("You are allowe dfor exam")
else:
     print("Invalid input")  

