
#rock paper  sissors

import random

user_wins = 0
computer_wins=0

options=["rock","paper","sissors"]

while True:
    user_input=input("choose rock/paper/sissors or Q to quite: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number=random.randint(0,2)

    computer_picks=options[random_number]

    print("computer_picked",computer_picks + ".")

    if user_input == "rocks" and computer_picks =="sissors":
        print("you won!")
        user_wins+=1
    elif user_input == "paper" and computer_picks =="rock":
        print("you won!")
        user_wins+=1
    elif user_input == "sissors" and computer_picks =="paper":
        print("you won!")
        user_wins+=1
    else:
        print("computer win")
        computer_wins+=1


print("you won",user_wins,"times.")
print("the computer won",computer_wins,"times.")
print("bye see u again ")
