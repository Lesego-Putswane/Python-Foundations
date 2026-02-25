'''
Task:Create a small program that:
Asks the user to enter:
Their exam score (0-100)
Their family income
Whether they completed community service (yes/no)

The program should:
If the score is 75 or higher → continue checking eligibility.
If the score is below 75 → print that they are not eligible for a scholarship.

If eligible academically:
If family income is below 300000 → continue evaluation.
If family income is 300000 or more → print that they do not qualify financially.
If they qualify financially:
If they completed community service → award Full Scholarship.
If they did not complete community service → award Partial Scholarship.'''

while True:
    try:
        exam_score = int(input("Enter your exam score: "))
        if exam_score >= 75:
            while True:
                try:
                    income = int(input("Enter your family income: "))
                    if income < 300000:
                        while True:
                            try:
                                community_service = input("Have you ever participated in any community service? yes(y) or no(n)): ").strip().lower()
                                if community_service in ["yes", "y"]:
                                    print("Congratulations! You have been awarded the Full Scholarship.")
                                elif community_service in ["no", "n"]:
                                    print("Congratulations! You have been awarded the Partial Scholarship.")
                                else:
                                    print("Invalid input. Please enter yes(n) or no(n)")
                            except ValueError:
                                print("Invalid input! Please enter the correct community service option.")
                    else:
                        print("Unfortunately due to your family finances, you do not qualify for the scholarship.")
                except ValueError:
                    print("Invalid input! Please enter the correct income.")
        else:
            print("Unfortunately your exam score is too low, therefore you do not qualify for the scholarship.")
    except ValueError:
        print("Invalid input! Please enter the correct score.")