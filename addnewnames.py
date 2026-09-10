import os # Importing OS Module for filesystem modifications

os.chdir("namelist/oldnames/")
f1 = open("names1.txt", "r")
c1 = f1.read()

os.chdir("..")
os.mkdir("newnames")
os.chdir("newnames")

f2 = open("names2.txt", "w")
c2 = c1 + "\n" + "Masseeha\n" + "Aqsa\n" + "CS\n"
f2.write(c2)

f1.close()
f2.close()

