from random import randint
######################################
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

user_move = input("MV > ") # To be continued!