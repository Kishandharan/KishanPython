from subprocess import run, DEVNULL
from os import mkdir, chdir

def exec_command(command):
    run(
        command.split(" "),
        check=True,
        shell=True,
        stdout=DEVNULL,
        stderr=DEVNULL,
    )

def write_file(fname, content):
    file = open(fname, "w")
    file.write(content)
    file.close()

def read_file(fname):
    file = open(fname, "r")
    contents = file.read()
    file.close()
    return contents

projectName = input("Enter Project Name: ")
appName = input("Enter App Name: ")
str1 = f"django-admin startproject {projectName}"
str2 = f"django-admin startapp {appName}"

exec_command(str1)
chdir(projectName)
exec_command(str2)
chdir(projectName)

old = read_file("settings.py")
str1 = "'django.contrib.staticfiles',"
str2 = f"'django.contrib.staticfiles',\n\t'{appName}',"
new = old.replace(str1, str2)
write_file("settings.py", new)

old = read_file("urls.py")
str1 = "from django.urls import path"
str2 = "from django.urls import path,include"
new = old.replace(str1, str2)
str1 = "path('admin/', admin.site.urls),"
str2 = f"path('admin/', admin.site.urls),\n\tpath('{appName}/', include('{appName}.urls'))"
new = new.replace(str1, str2)
write_file("urls.py", new)

chdir(f"../{appName}")
mkdir("templates")
chdir("templates")
mkdir(appName)
chdir(appName)
write_file("index.html", '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django</title>
</head>
<body>
    <p>Hello World</p> 
    <p>{{param1}}</p>   
</body>
</html>
''')

chdir("../..")
old = read_file("views.py")
str1 = "# Create your views here."
str2 = f'''def home(request):
\tnum1 = 5
\tfact1 = fact(num1)
\treturn render(request, '{appName}/index.html', {{'param1': fact1}})

def fact(num1):
\tresult = num1
\tfor i in range(result-1, 0, -1):
\t\tresult = result * i
\treturn result
'''
new = old.replace(str1, str2)
write_file("views.py", new)

write_file("urls.py", f'''from django.urls import path
from {appName}.views import home
urlpatterns = [path('', home)]           
''')