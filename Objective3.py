# Objective 3: Leap Year Explorer

#Task 1: Leap Year Checker

# Given an input Year, check to see if that year is a leap year. All Leap Years are divisible by 4, with the exception of years that are exactly divisble by 100.

# Expected Outcome: If you test the year 1900, is should be False. The year 2000 should be True. The year 2024 should be True

year = input(f"Hello User! Please input a year and I will tell you if that year is a Leap Year.")

year = int(year) # Ensure the data type is correct, passing a string gave me an error the first time.

if year % 4 == 0 and year % 100 != 0: # Check to see if year is divisible by 4
    print(f"The year {year} is a Leap Year!")
elif year % 400 == 0: # Check if its divisible by 400
    print(f"The year {year} is a Leap Year!")
else: #Otherwise...
    print(f"The year {year} is not a Leap Year.")    
