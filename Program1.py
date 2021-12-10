#Create a program that ask 3 numbers (0-9) from the user.
#Generate 3 random winning numbers (0-9)
#Display “Winner” if all 3 input numbers matched the generated numbers
#Display ”You loss” if not
#Display ”Try again y/n” after each game
#If the user enter “y” the user will lottery again
#if “n” the program will exit.

import random
import time 

print("LOTTERY")
time.sleep(1)
print("WELCOME TO LOTTERY GAME!")

time.sleep(2)
name = input("Enter your name: ")
print(f"HI {name}, GUESS A THREE NUMBER BETWEEN 0 - 9 TO WIN!")
time.sleep(2)
print(f"{name}, GET READY TO GUESS!")

time.sleep(3)
lottery = True
while lottery:
    first = int(input("Enter your First number: "))
    second = int(input("Enter your Second number: "))
    third = int(input("Enter your Third number: "))

    one = random.randint(0,9)
    two = random.randint(0,9)
    three = random.randint(0,9)
    
    user_number = first, second, third
    random_number = (one, two, three)
    time.sleep(2)
    if  user_number == one and two and three:
        print(f"CONGRATULATIONS {name}! YOU WIN THE LOTTERY!")
        print(random_number)
    else:
        print(f"Winning Numbers: {random_number}")        
        print(f"Your Numbers: {user_number}")
        print(f"BETTER LUCK NEXT TIME {name}! YOU LOSS THE LOTTERY!")

    time.sleep(3)
    user_answer = input(f"ENTER 'yes' TO PLAY AGAIN AND 'no' TO EXIT THE GAME: ").lower()
    while True:
        if user_answer == "yes":
            lottery = True
            break
        elif user_answer == "no":
            lottery = False
            break

print("-THANK YOU FOR PLAYING LOTTERY GAME-")
