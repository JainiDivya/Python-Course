# import random
# print(random.choice('computer')) #gives you a letter from the given word

# print(random.randint(1,100)) #prints number within 1-100

# print(random.random())  #prints a random float number

# import random
# # using random() to generate a random number
# # between 0 and 1
# print("The random number between 0 and 1 is : ", end="")

# print(random.random())

# # using seed() to seed a random number
# print(random.seed(11))

# import random #importing module
# playing = True #initialise
# # number = str(random.randint(0,9)) #random in-built function
# number = random.randint(0,9) #random in-built function
# print("the answer is" , number)

# print("I will generate a number from 0 to 9, and you have to guess the number one digit at a time.")
# print("The game ends when you get 1 hero!")
# #iterate loop till the condition is true    
# while playing:
#   guess = input("Give me your best guess! \n")
#   if number == guess:
#     print("You win the game")
#     print("The number was",number)
#     break 
    
#   else:
#     print("Your guess isn't quite right, try again. \n")

import math #importing math module
#using ceil and floor functiom of math module
print('The Floor and Ceiling value of 23.56 are: ' + str(math.ceil(23.56)) + ', ' + str(math.floor(23.56)))

x = 10
y = -15
#using copysign function
print('The value of x after copying the sign from y is: ' + str(math.copysign(x, y)))

#using fabs and gcd function
print('Absolute value of -96 and 56 are: ' + str(math.fabs(-96)) + ', ' + str(math.fabs(56)))

print('The GCD of 24 and 56 : ' + str(math.gcd(24, 56)))

