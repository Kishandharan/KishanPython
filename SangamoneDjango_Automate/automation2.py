import subprocess
import os

def execute_command(command):
    subprocess.run(
        command.split(" "),
        check=True,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

pName = input("Enter project name💥💥🎨: ")
aName = input("Enter app name💥💥🎨: ")

execute_command(f"django-admin startproject {pName}")
os.chdir(pName)
execute_command(f"django-admin startapp {aName}")

os.chdir(pName)
file1 = open("settings.py", "r+")
old1 = file1.read()
s1 = "'django.contrib.staticfiles',"
s2 = s1+"\n    " + f"'{aName}'"
new1 = old1.replace(s1, s2)
file1.seek(0)
file1.write(new1)
file1.close()

