'''
Task: Write a Python program that:
Takes a year input from the user.
Determines whether the year is a leap year or not.
Leap year rules:
A year is a leap year if:
It is divisible by 4 and not divisible by 100, or
It is divisible by 400'''

year = int(input("Enter a year: \n"))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")