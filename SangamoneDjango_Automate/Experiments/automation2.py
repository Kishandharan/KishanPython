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

if not os.path.isdir(pName):
    execute_command(f"django-admin startproject {pName}")
os.chdir(pName)
if not os.path.isdir(aName):
    execute_command(f"django-admin startapp {aName}")
else:
    print(f"\nSorry, but the app name {aName} is already taken by another app!")
    print("Please try again with a different app name!")

os.chdir(pName)
file1 = open("settings.py", "r+")
old1 = file1.read()
s1 = "'django.contrib.staticfiles',"
s2 = s1+"\n    " + f"'{aName}'"
new1 = old1.replace(s1, s2)
file1.seek(0)
file1.write(new1)
file1.close()

file1 = open("urls.py", "r+")
old1 = file1.read()
new1 = ""
s1 = "path('admin/', admin.site.urls),"
s2 = s1+f"\n    path('{aName}', include('{aName}.urls'))"
new1 = old1.replace(s1, s2)
s1 = "from django.urls import path"
s2 = "from django.urls import path,include"
new1 = new1.replace(s1, s2) 
file1.seek(0)
file1.write(new1)
file1.close()

os.chdir(f"../{aName}")
os.mkdir("templates")
os.chdir("templates")
os.mkdir(aName)
os.chdir(aName)
file1=open("index.html", "w")
file1.write('''
<!DOCTYPE HTML>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello World Django Project</title>
</head>
<body>
    <h1>Automated Django App</h1>
    <p>{{param1}}</p>
</body>
</html>
''')
file1.close()

os.chdir("../..")
file1=open("views.py", "w")
file1.write(f'''
from django.shortcuts import render

def home(request):
    return render(request,'{aName}/index.html',{{'param1':'hello world'}})
''')
file1.close()

file1=open("urls.py", "w")
file1.write(f'''
from django.urls import path
from {aName}.views import home
urlpatterns = [path('', home),]
''')
file1.close()
