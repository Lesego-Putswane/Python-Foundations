'''
Task: Divisibility Patterns
Goal:Ask the user to enter a positive number N.
Loop from 1 to N.
For each number:
If divisible by 2, print "divisible by 2"
If divisible by 3, print "divisible by 3"
If divisible by 5, print "divisible by 5"
If divisible by more than one, print them separated by commas.
If not divisible by any of them, just print the number.

Practice using:
The modulus operator %
Loops (for)
Multiple condition checks
Logical operators (and)
Clean output formatting
Program Requirements
'''

user_number = int(input("Enter a number: "))

for number in range(1, user_number+1):
    divisors = []

    if number % 2 == 0:
        divisors.append("2")
    if number % 3 == 0:
        divisors.append("3")
    if number % 5 == 0:
        divisors.append("5")
    
    if divisors:
        print(f"{number} divisible by {','.join(divisors)}")
    else:
        print(number)