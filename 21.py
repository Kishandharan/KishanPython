import os
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
            os.mkdir(args[2])
            os.chdir(args[2])
            file=open(args[2], "w")
            os.chdir("../..")
            org_filecontent=open(args[2],"r").read()
            os.chdir(f".ftt/{args[2]}")
            file.write(org_filecontent)
            os.chdir("../..")
