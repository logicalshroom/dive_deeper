# Objective 2: The Greatest Showdown
# Task 1: Identify The Greatest

# Write a program that asks the user to enter 3 numbers, and then identifies and prints the largest number.
print("Task 1 starts here.")

#First lets request user inputs
print(f"Hello, User! Please enter 3 numbers, one at a time. I will tell you which one is the Greatest!")
num1 = int(input("Please input the first number."))
num2 = int(input("Please input the second number."))
num3 = int(input("Please input the third number."))

#Once we have numbers, we can definte the function that will check the greatest number
def largest(num1,num2,num3):
    if num1 >= num2 and num1 >= num3: # If num1 is greater than num2 AND num3, print the following
        print(f"The greatest number is {num1}!")
    elif num2 >= num1 and num2 >= num3: # If num2 is greater than num1 AND num3, print the following
        print(f"The greatest number is {num2}!")
    else: # If num 1 and num 2 are not the greatest, then it must be num 3.
        print(f"The greatest number is {num3}!")

largest(num1,num2,num3)

# Task 2: Identify The Smallest

# Improve your code, and also print the smallest number.

# We already have inputs, so we can skip that part here.

# We are gonna name a new function...

print(f"Task 2 Starts here.")

def bignsmall(num1,num2,num3):
    if num1 >= num2 and num1 >= num3: 
        print(f"The greatest number is {num1}!")
    elif num2 >= num1 and num2 >= num3:
        print(f"The greatest number is {num2}!")
    else:
        print(f"The greatest number is {num3}!")
    if num1 <= num2 and num1 <= num3: #Lets just use the same function as before but in reverse and a second time
        print(f"The smallest number is {num1}!")
    elif num2 <= num1 and num2 <= num3: 
        print(f"The smallest number is {num2}!")
    else: 
        print(f"The smallest number is {num3}!")


bignsmall(num1,num2,num3)