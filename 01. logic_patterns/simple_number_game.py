'''
Task:Create a small program that:
Asks the user to guess a secret number.
If the guess is correct → print a success message.
If the guess is too high → tell them it's too high.
If the guess is too low → tell them it's too low.
Keep asking until they guess correctly.
You choose:
The secret number can be hardcoded (like 7 or 15).
Or you can use random if you want extra challenge.'''

secret_number = 79


while True:
    user_number = int(input("Enter a number: "))

    if user_number == secret_number:
        print(f"Good job! {user_number} is the secret number.")
        break
    elif user_number > secret_number:
        print(f"{user_number} is too HIGH. Try again.")
    else:
        print(f"{user_number} is too LOW. Try again.")
