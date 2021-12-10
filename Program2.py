# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

import random

print("GUESS THE NUMBER")
print("ELCOME TO GUESS A NUMBER GAME!")

name = input("Enter your name: ")
print(f"HI {name}, GUESS A NUMBER BETWEEN 0 - 100 TO WIN!")
print(f"{name}, GET READY TO GUESS!")

user_number = int(input("Your Guess Number: "))
random_number = random.randint(0,100)

while random_number != user_number:
    if user_number < random_number:
        print("Guess Greater Than Your Input Number.")
        user_number = int(input("Enter Again Your Guess Number: "))
        if user_number == random_number:
            print(f"RANDOM NUMBER: {random_number}")
            print(f"CONGRATULATIONS {name}! YOU GUESS THE CORRECT NUMBER!")
            break
    elif user_number > random_number:
        print("Guess Less Than Your Input Number.")
        user_number = int(input("Enter Again Your Guess Number: "))
        if user_number == random_number:
            print(f"RANDOM NUMBER: {random_number}")
            print(f"CONGRATULATIONS {name}! YOU GUESS THE CORRECT NUMBER!")
            break

print("-THANK YOU FOR PLAYING GUESS THE NUMBER-")
