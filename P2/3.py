import os
import shutil
os.chdir("C:/")
#Difference between os.rmdir and shutil.rmtree
#shutil.rmtree  -    This deletes Folders and it's contents
#os.rmdir       -    This can delete only empty folders 

while True:
    command = input(">>")
    if command.startswith("cd"):
        path = command.split(" ",1)[1]
        os.chdir(path)
        #For changing the current working directory

    if command.startswith("mkdir"):
        directory_name = command.split(" ",1)[1]
        os.mkdir(directory_name)
        #For creating Directories

    if command.startswith("rmdir"):
        directory_name = command.split(" ",1)[1]
        shutil.rmtree(directory_name)
        #For removing directories

    if command.startswith("cf"):
        file_name = command.split(" ",1)[1]
        f1 = open(file_name, "x")
        f1.close()
        #For creating files

    if command.startswith("df"):
        file_name = command.split(" ",1)[1]
        os.remove(file_name)
        #For deleting files

    if command.startswith("wf"):
        file_name = command.split(" ", 1)[1]
        f1 = open(file_name, "w")
        while True:
            content = input("c>>")
            if content == "quit":
                break
            f1.write(content+"\n")
        f1.close()
        #For writing to files

    if command.startswith("af"):
        file_name = command.split(" ", 1)[1]
        f1 = open(file_name, "a")
        while True:
            content = input("c>>")
            if content == "quit":
                break
            f1.write(content+"\n")
        f1.close()
        #For adding content to files

    if command.startswith("rf"):
        file_name = command.split(" ", 1)[1]
        f1 = open(file_name, "r")
        print(f1.read())
        f1.close()
        #For reading files

    if command.startswith("rnf"):
        oldname = command.split(" ", 1)[1]
        newname = input("newname>>")
        os.rename(oldname,newname)
        #For renaming files and folders

    if command == "ld":
        for ff in os.listdir():
            print(ff)
        #For getting all the files and folders available

    if command == "wlk":
        print(list(os.walk(os.getcwd())))
        
    if command == "getcwd":
        print(os.getcwd())
        #For getting the current working directory

    if command == "quit" :
        break
        #For quiting the app
