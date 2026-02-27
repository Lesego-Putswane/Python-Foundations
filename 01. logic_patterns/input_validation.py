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
    name = input("Enter your full name: ").strip().title()
    if name != "":
        break
    else:
        print("Name can not be empty. Please try again")

age = 4
email = "le@gmail.com"
phone = 9475862936

print(f"\nRegistration Successful! \nName: {name} \nAge: {age} \nEmail: {email} \nPhone: {phone}")