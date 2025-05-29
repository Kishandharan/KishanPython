import os
import shutil
import sys

args = sys.argv
commands = ["backup"]

if not os.path.isdir(".ftt"):
    os.mkdir(".ftt")
if not args[1] in commands:
    print("Oops! That looks like a invalid command! Please try again.")
    exit()
else:
    if args[1] == "backup":
        if os.path.isfile(args[2]):
            os.chdir(".ftt")
            if not os.file.isdir(args[2]):
                os.mkdir(args[2])
            os.chdir(args[2])
            if not os.path.isfile(".lstct"):
                lstct_file=open(".lstct", "w")
                lstct_file.write("1")
                lstct="1"
            else:
                lstct_file=open(".lstct", "r")
                lstct=lstct_file.read()
            file=open(args[2]+lstct, "w")
            shutil.copyfile(f"../../{args[2]}", f"./{args[2]+lstct}")
            os.chdir("../")
    if args[1] == "restore":
        #To be continued...

