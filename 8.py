from random import randint
######################################
user_add_confirm = ""
user_confirm_all = False
user_move = ""
row = 0
item = 0
user_number = 0
game_matrix = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]


for x in game_matrix:
    for y in range(0, len(x)):
        x[y] = randint(0, 100)

for z in game_matrix:
    print(z)

for g in range(0, 5):
    user_move = input("MV > ") # <row>-<row-item>, Example: 1-1
    row = int(user_move.split("-")[0])-1
    item = int(user_move.split("-")[1])-1
    if not user_confirm_all:
        user_add_confirm = input(f"Move to {game_matrix[row][item]} ([Y]es, [N]o, [A]ll)?").lower()
        if user_add_confirm == "y":
            pass
        elif user_add_confirm == "n":
            continue
        elif user_add_confirm == "a":
            user_confirm_all = True
        else:
            print("Oops! It looks like you have entered something invalid! So we are defaulting to NO!")
            continue


