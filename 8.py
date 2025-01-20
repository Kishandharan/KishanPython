from random import randint
import sys
######################################
computer_number = 0
rounds = int(input("How many rounds do you want to play? "))
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
    if user_number >= game_matrix[row][item]:
        user_number = user_number + game_matrix[row][item]
    else:
        print("Oops! You lost! Because the number you chose was more powerful than you!")
        sys.exit()
    if g != rounds:
        print(f"Your current score: {user_number}")

print()
computer_number = randint(0, 800)
if computer_number > user_number:
    print(f"Oops! You lost! Because the computer became more powerful than YOU!")
else:
    print("Yay! YOU won!")
print(f"Computer: {computer_number}")
print(f"You: {user_number}")
