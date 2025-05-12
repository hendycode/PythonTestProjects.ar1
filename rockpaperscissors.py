import random

userwins = 0
compwins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    randomno = random.randint(0, 2)
    # rock:0, paper:1, scissors:2

    computer_pick = options[randomno]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        userwins += 1


print("Goodbye!")
