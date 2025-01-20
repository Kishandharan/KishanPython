from random import randint
from time import sleep
import sys
######################################
computer_number = 0
used_moves = []
rounds = int(input("How many rounds do you want to play? "))
if rounds > 45:
    print("This prompt cannot be over 45!")
    sleep(5)
    sys.exit()
user_add_confirm = ""
user_confirm_all = False
user_move = ""
row = 0
item = 0
user_number = 100
game_matrix = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]
print("We gave you 100 points to help you get started!")
print()
for x in game_matrix:
    for y in range(0, len(x)):
        x[y] = randint(0, 800)

for z in game_matrix:
    print(z)

for g in range(0, rounds):
    user_move = input("MV > ") # <row>-<row-item>, Example: 1-1
    if user_move not in ["exit", "disp_matrix"]:
        row = int(user_move.split("-")[0])-1
        item = int(user_move.split("-")[1])-1
        if not user_confirm_all:
            user_add_confirm = input(f"Move to {game_matrix[row][item]} ([Y]es, [N]o, [A]ll)?").lower()
            if user_add_confirm == "y":
                pass
            elif user_add_confirm == "n":
                print(user_number)
                continue
            elif user_add_confirm == "a":
                user_confirm_all = True
            else:
                print("Oops! It looks like you have entered something invalid! So we are defaulting to NO!")
                continue
        if not (user_move in used_moves):
            if user_number >= game_matrix[row][item]:
                user_number = user_number + game_matrix[row][item]
                used_moves.append(user_move)
            else:
                print("Oops! You lost! Because the number you chose was more powerful than you!")
                sys.exit()
        else:
            print("Oops! It looks like you are trying to move to a point which you already used! Try again!")
    else:
        if user_move == "disp_matrix":
            for z in game_matrix:
                print(z)
        if user_move == "exit":
            sys.exit()

    if g != (rounds - 1):
        print(f"Your current score: {user_number}")

print()
computer_number = randint(0, 800)
if computer_number > user_number:
    print(f"Oops! You lost! Because the computer became more powerful than YOU!")
else:
    print("Yay! YOU won!")
print(f"Computer: {computer_number}")
print(f"You: {user_number}")
