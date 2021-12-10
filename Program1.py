#Create a program that ask 3 numbers (0-9) from the user.
#Generate 3 random winning numbers (0-9)
#Display “Winner” if all 3 input numbers matched the generated numbers
#Display ”You loss” if not
#Display ”Try again y/n” after each game
#If the user enter “y” the user will lottery again
#if “n” the program will exit.

import random
import time 

print("\033[1;37;1mLOTTERY\033[0m")
time.sleep(1)
print("\n\033[1;35;1mWELCOME TO LOTTERY GAME!\033[0m")

time.sleep(2)
name = input("\n\33[1;32;1mEnter your name:\33[0m ")
print(f"\n\033[1;35;1mHI \033[1;37;1m{name}\033[0m, \033[1;35;1mGUESS A THREE NUMBER BETWEEN 0 - 9 TO WIN!\033[0m")
time.sleep(2)
print(f"\n\033[1;37;1m{name},\033[0m \033[1;35;1mGET READY TO GUESS!\033[0m")

time.sleep(3)
lottery = True
while lottery:
    first = int(input("\n\033[1;33;3mEnter your First number:\33[0m "))
    second = int(input("\033[1;33;3mEnter your Second number:\33[0m "))
    third = int(input("\033[1;33;3mEnter your Third number:\33[0m "))

    one = random.randint(0,9)
    two = random.randint(0,9)
    three = random.randint(0,9)
    
    user_number = first, second, third
    random_number = (one, two, three)
    time.sleep(2)
    if  user_number == one and two and three:
        print(f"\n\033[1;34;1mCONGRATULATIONS \033[1;37;1m{name}\033[0m! \033[1;34;1m YOU WIN THE LOTTERY!\033[0m")
        print(random_number)
    else:
        print(f"\n\033[1;31;3mWinning Numbers: {random_number}\33[0m")        
        print(f"\033[1;31;3mYour Numbers: {user_number}\33[0m")
        print(f"\n\033[1;31;1mBETTER LUCK NEXT TIME \033[1;37;1m{name}\033[0m! \033[1;31;1mYOU LOSS THE LOTTERY!\033[0m")

    time.sleep(3)
    user_answer = input("\n\033[1;35;1mENTER \033[1;37;1m'yes'\033[0m \033[1;35;1mTO PLAY AGAIN AND \033[1;37;1m'no'\033[0m \033[1;35;1mTO EXIT THE GAME:\033[0m ").lower()
    while True:
        if user_answer == "yes":
            lottery = True
            break
        elif user_answer == "no":
            lottery = False
            break

time.sleep(2)
print("\n\033[1;37;1m-THANK YOU FOR PLAYING LOTTERY GAME-\033[0m")
