import sys

args = sys.argv
fname = args[1]
lines = open(fname, "r").readlines()

for line in lines:
    tokens = line.split(" ")
    if tokens[0] == "set":
        eval(f"{tokens[1]} = {tokens[2].replace(";","")}") # THIS IS UNSAFE, will find an alternative soon
        print(eval(f"{tokens[1]}"))
