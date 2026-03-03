'''
Task:
Write a Python program that:
Takes a score input from the user (0-100).
Prints the grade based on these rules:
90-100 → "A"
80-89 → "B"
70-79 → "C"
60-69 → "D"
Below 60 → "F"'''

score = int(input("Enter your score (1-100): "))

if score > 100 or score < 0:
    print("Score is out of range! Please enter a score between 1 and 100.")
elif score >= 90:
    print(f"Your score of {score}, puts you in A grade. Excellent job.")
elif score >= 80:
    print(f"Your score of {score}, puts you in B grade. Great job, theres still room for improvement.")
elif score >= 70:
    print(f"Your score of {score}, puts you in C grade. Good job, You can do better")
elif score >= 60:
    print(f"Your score of {score}, puts you in D grade. Well done, but please pull up your socks")
else:
    print(f"Your score of {score}, puts you in F grade. It's not the end, There's still hope")