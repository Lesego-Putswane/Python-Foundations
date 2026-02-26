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
        medical_check = input("“Do you have doctor approval?” (yes/no): ").lower()
        if medical_check in ["yes", "y", "no", "n"]:
            break
        else:
            print("Invalid input! Please enter yes(y) or no(n)")
    
    if medical_check in ["no", "n"]:
        print("Due to your medical check results, your membership application has been DENIED!")
    else:
        while True:
            try:
                income = int(input("Enter your income: "))
                if income >= 2000:
                    print("Congratulations. You hae been aproved for the PREMIUM memebership.")
                    break
                elif income < 2000:
                    print("Congratulations. You hae been aproved for the BASIC memebership.")
                    break
                else:
                    print("Income can not be less than 0!")
            except ValueError:
                print("Invalid input provided! Please enter correct income value above 0")