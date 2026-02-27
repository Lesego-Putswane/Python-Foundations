'''
Task
Create a program that asks the user for:
Age, Monthly income, Do they have a medical condition? (yes/no)

Rules
Step 1 - Age Check
If age < 16
→ Reject immediately (too young)
If age ≥ 16
→ Continue

Step 2 - Medical Check
If they have a medical condition:
Ask: “Do you have doctor approval?” (yes/no)
If no → Reject
If yes → Continue
If they do NOT have a medical condition
→ Continue automatically

Step 3 - Financial Check
If income ≥ 2000
→ Approve Premium Membership
If income < 2000
→ Approve Basic Membership
'''

print("Welcome to the membership system!")

while True:
    try:
        age = int(input("Enter your age: "))
        if age > 0:
            break
        else:
            print("Age can't be less than zero(0)")
    except ValueError:
        print("Invalid age provided! Please provide valid age.")

if age < 16:
    print("Membership registration terminated! You are too young to join the gym.")
else:
    while True:
        medical_condition = input("\nDo you have a medical condition? yes(y) / no(n): ").lower()
        if medical_condition in ["yes", "y","no", "n"]:
            break
        else:
            print("Invalid option! Please enter yes(y) / no(n)")

    if medical_condition in ["yes", "y"]:
        while True:
            doctor_approval = input("\nDo you have doctor approval? (yes/no): ").lower()
            if doctor_approval in ["yes", "y"]:
                break
            elif doctor_approval in ["no", "n"]:
                print("Unfortunately, without a doctors approval we can not continue your registration!")
                exit()
            else:
                print("Invalid option! Please enter yes(y) / no(n)")

    while True:
        try:
            income = int(input("\nEnter your income: "))
            if income < 0:
                print("Income can not be less than 0!")
            elif income >= 2000:
                print("Congratulations. You have been aproved for the PREMIUM memebership.")
                break
            else:
                print("Congratulations. You have been aproved for the BASIC memebership.")
                break
        except ValueError:
            print("Invalid input provided! Please enter correct income value above 0")
