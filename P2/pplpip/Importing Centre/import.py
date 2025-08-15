import os
os.chdir("C:\\Coding\\Python\\pplpip\\Store")
command = input(">>")
if command.startswith("import"):
	filename = command.split(" ", 1)[1]
	fdata = ""
	f1 = open(filename, "r")
	fdata = f1.read()
	os.chdir("C:\\Coding\\Python\\pplpip\\My data")
	f2 = open(filename, "x")
	f3 = open(filename, "w")
	f3.write(fdata)
	