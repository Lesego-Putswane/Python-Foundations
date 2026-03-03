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
def user_name():
    print("----------Welcome to user registration----------")
    while True:
        name = input("\nEnter your full name: ").strip().title()
        if name != "":
            return name
        else:
            print("Name can not be empty. Please try again")

def user_age():
    while True:
        try:
            age = int(input("\nEnter your age: "))
            if age >= 0:
                return age
            else:
                print("Age can not be less than 0. Please try again.")
        except ValueError:
            print("Invalid Input! Please enter a numerical value.")

def user_email():
    while True:
        email = input("\nEnter your email: ").strip().lower()

        if email.count("@") != 1:
            print("Invalid email. There must be exactly one '@' symbol.")
            continue

        at_index = email.index("@")

        if at_index == 0 or at_index == len(email) - 1:
            print("Invalid email format.")
            continue

        domain_part = email[at_index + 1:]

        if "." not in domain_part:
            print("Invalid email. Domain must contain a '.'")
            continue

        return email
def phone_number():
    while True:
        phone = input("\nEnter your valid 10 digits phone number: ")
        if len(phone) == 10 and phone.isdigit():
            return phone
        else:
            print("Your phone number must contain 10 digits! Please try again.")
    
name = user_name()
age = user_age()
email = user_email()
phone = phone_number()

print("\nRegistration Successful!")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Email: {email}")
print(f"Phone: {phone}")