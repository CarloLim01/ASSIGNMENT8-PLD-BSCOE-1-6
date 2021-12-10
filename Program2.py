# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

import random
import time

print("\033[1;37;1mGUESS THE NUMBER\033[0m")
time.sleep(1)
print("\n\033[1;35;1mWELCOME TO GUESS A NUMBER GAME!\033[0m")

time.sleep(2)
name = input("\n\33[1;32;1mEnter your name:\33[0m ")
print(f"\n\033[1;35;1mHI \033[1;37;1m{name}\033[0m, \033[1;35;1mGUESS A NUMBER BETWEEN 0 - 100 TO WIN!\033[0m")
time.sleep(2)
print(f"\n\033[1;37;1m{name},\033[0m \033[1;35;1mGET READY TO GUESS!\033[0m")

time.sleep(3)
user_number = int(input("\n\033[1;33;3mYour Guess Number:\33[0m "))
random_number = random.randint(0,100)

while random_number != user_number:
    if user_number < random_number:
        time.sleep(1)
        print("\n\033[1;31;3mGuess Greater Than Your Input Number.\33[0m")
        time.sleep(1)
        user_number = int(input("\n\033[1;33;3mEnter Again Your Guess Number:\33[0m "))
        if user_number == random_number:
            time.sleep(2)
            print(f"\n\033[1;34;1mRANDOM NUMBER:\033[0m \033[1;37;1m{random_number}\033[0m")
            time.sleep(2)
            print(f"\n\033[1;34;1mCONGRATULATIONS \033[1;37;1m{name}\033[0m! \033[1;34;1mYOU GUESS THE CORRECT NUMBER!\033[0m")
            break
    elif user_number > random_number:
        time.sleep(1)
        print("\n\033[1;31;3mGuess Less Than Your Input Number.\33[0m")
        time.sleep(1)
        user_number = int(input("\n\033[1;33;3mEnter Again Your Guess Number:\33[0m "))
        time.sleep(2)
        if user_number == random_number:
            print(f"\n\033[1;34;1mRANDOM NUMBER:\033[0m \033[1;37;1m{random_number}\033[0m")
            time.sleep(2)
            print(f"\n\033[1;34;1mCONGRATULATIONS \033[1;37;1m{name}\033[0m! \033[1;34;1mYOU GUESS THE CORRECT NUMBER!\033[0m")
            break
        
time.sleep(2)
print("\n\033[1;37;1m-THANK YOU FOR PLAYING GUESS THE NUMBER-\033[0m")
