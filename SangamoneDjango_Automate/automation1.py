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

pName = input("Enter your project name🚀🚀🧑‍💻🤓: ")
aName = input("Enter your app name🚀🚀🧑‍💻🤓: ")

execute_command(f"django-admin.exe startproject {pName}")
os.chdir(pName)
execute_command(f"django-admin.exe startapp {aName}")
os.chdir(pName)

file = open("settings.py", "r+")
old_content = file.read()
new_content = old_content.replace("""'django.contrib.staticfiles',""", f"""'django.contrib.staticfiles',\n    '{aName}' """)
file.seek(0)
file.write(new_content)
file.close()

file = open("urls.py", "r+")
old_content = file.read()
new_content = old_content.replace("from django.urls import path", "from django.urls import path,include").replace("path('admin/', admin.site.urls)", f"path('admin/', admin.site.urls),\n    path('{aName}/', include('{aName}.urls'))")
file.seek(0)
file.write(new_content)
file.close()

os.chdir(f"../{aName}")
os.mkdir("templates")
os.chdir("templates")
os.mkdir(aName)
os.chdir(aName)
file=open("index.html", "w")
file.write("""<!DOCTYPE HTML>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello World</title>
</head>
<body>
    <p>Hello World</p>
    <p>{{param1}}</p>
</body>
""")
file.close()

os.chdir("../..")
file=open("views.py", "r+")
old_content=file.read()
new_content=old_content.replace("# Create your views here.",f"""def home(request):\n    return render(request,'{aName}/index.html',{{'param1':"hello world"}})""")
file.seek(0)
file.write(new_content)
file.close()

file=open("urls.py", "w")
file.write(f"""from django.urls import path
from {aName}.views import home
urlpatterns = [path('', home),]""")
file.close()

print("\nProject Creation Done!!")

