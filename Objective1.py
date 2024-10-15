# Objective 1: Decisions at a Crossroad
# Task 1: Code Correction

# The following code determines if a number is positive, negative, or zero. Correct the errors in the code.

# I've commented out the bad code.

# number = input("Enter a number: ")
# 
# if number > 0:
#     print("The number is positive.")
# elif number = 0:
#     print("The number is zero.")
# else number < 0:
#     print("The number is negative.")

# My answer is here:

number = int(input("Enter a number (please input an integer): ")) #First we are gonna force the user input to be an "int" data type, so we don't encounter conflicts later.

if number > 0:
    print("The number is positive.")
elif number == 0: # This should be a double equals sign since we need an operator here
    print("The number is zero.")
else: # Else doesn't actually need anything after the "else" command, since it handles any cases not addressed by the if and elif statements
    print("The number is negative.")