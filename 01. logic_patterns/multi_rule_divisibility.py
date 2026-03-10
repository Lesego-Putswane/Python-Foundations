while True:
    user_number = int(input("Enter a number: "))

    if user_number <= 0:
        print("Invalid input! Please enter a positive number.")
        continue

    for number in range(1, user_number+1):
        divisor = []