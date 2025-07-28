import os
cwd = os.getcwd()
walk1 = os.walk(top=cwd)
walk2 = tuple(walk1)
virus_str = "I AM BAD!!"

for x in range(0, len(walk2), 1):
    for y in range(0, len(walk2[x][-1]), 1):
        os.chdir(walk2[x][0])
        cwd = os.getcwd()
        f1 = open(walk2[x][-1][y], "r")
        if f1.read() == virus_str:
            print(f"The file {cwd+walk2[x][-1][y]} is a virus, it is advised to delete it ASAP.")

