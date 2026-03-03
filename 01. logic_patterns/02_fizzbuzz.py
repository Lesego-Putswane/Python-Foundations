'''
Task:Write a Python program that:
Loops through numbers from 1 to 20.
Prints:
"Fizz" if the number is divisible by 3
"Buzz" if the number is divisible by 5
"FizzBuzz" if the number is divisible by both 3 and 5
The number itself if none of the above'''

for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)