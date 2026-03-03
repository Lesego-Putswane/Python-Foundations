'''
Exercise: Even or Odd Checker
Goal: Practice simple conditional logic (if/else)
Task:
Write a Python program that:
Takes a number input from the user.
Prints "Even" if the number is divisible by 2.
Prints "Odd" if the number is not divisible by 2.'''

number = int(input("Enter any number of your choice: \n"))

if number % 2 == 0:
    print(f"The number {number}, is an EVEN number.")
else:
    print(f"The number {number}, is an ODD number.")