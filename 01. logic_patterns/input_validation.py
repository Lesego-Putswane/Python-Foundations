'''
Task: Input Validation Practice
Goal: Practice validating user input using conditionals and try/except.
Program Requirements:
Ask the user for:
Name (non-empty string)
Age (integer ≥ 0)
Email (must contain @ and .)
Phone number (digits only, exactly 10 digits)
For each input, check if it is valid:
If valid, move to the next input.
If invalid, print a clear error message and ask again.
After all inputs are valid, print a summary:
Registration Successful!
Name: <name>
Age: <age>
Email: <email>
Phone: <phone>
'''

print("----------Welcome to user registration----------")
while True:
    name = input("\nEnter your full name: ").strip().title()
    if name != "":
        break
    else:
        print("Name can not be empty. Please try again")

while True:
    try:
        age = int(input("\nEnter your age: "))
        if age >= 0:
            break
        else:
            print("Age can not be less than 0. Please try again.")
    except ValueError:
        print("Invalid Input! Please enter a numerical value.")

while True:
    email = input("\nEnter your email: ").strip().lower()
    if "@" in email and "." in email:
        break
    else:
        print("Invalid email provided. Enter a valid email that contains '@' and '.'")

phone = 9475862936

print(f"\nRegistration Successful! \nName: {name} \nAge: {age} \nEmail: {email} \nPhone: {phone}")