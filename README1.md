# Automation

Please find automation1.py at https://github.com/Kishandharan/KishanPython/blob/main/django_automation/automation1.py
This contains the following:    
## 1. Import     
```
import subprocess    
import os     
```
Subprocess is a library that allows us to 
run shell processes from our code.       
For example, if we want to execute a command from our code, this library can do it.

## 2. Create function for executing commands    
```
def exec_command(command):    
    subprocess.run(command.split(" "),    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)    
```
a) The stdout argument tells subprocess where to throw the successful output of the command.    
b) The stderr argument tells subprocess where to throw the errors of the command.        
c) The check argument, if set to true, makes subprocess throw an error if the command does not work.    
## 3. Create function for writing files    
```
def write_file(fname, content):    
    f1=open(fname, "w")    
    f1.write(content)    
    f1.close()    
```


## 4. Create django project and app inside it    
```
project_name = input("Enter Project Name: ")    
app_name = input("Enter App Name: ")    
exec_command(f"django-admin startproject {project_name}")                      
os.chdir(project_name)                            
exec_command(f"django-admin startapp {app_name}")    
os.chdir(project_name)    
```




## 5. Write settings.py    
```
INSTALLED_APPS = [    
    'django.contrib.admin',    
    'django.contrib.auth',    
    'django.contrib.contenttypes',      
    'django.contrib.sessions',    
    'django.contrib.messages',    
    'django.contrib.staticfiles',    
    '{app_name}'    
]     

ROOT_URLCONF = '{project_name}.urls'    

WSGI_APPLICATION = '{project_name}.wsgi.application'    
```


## 6. Write urls.py    
```
from django.urls import path,include    

path('{app_name}/', include('{app_name}.urls')),    
```


## 7. Creating templates/app1    
```
os.chdir(f"../{app_name}")    
os.mkdir("templates")     
os.chdir("templates")    
os.mkdir(app_name)    
os.chdir(app_name)    
```
## 8. Writing Index.html    
```
write_file("index.html", '''    
<!DOCTYPE html>
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
```


## 9. Writing app1/views.py    
```    
os.chdir("../..")    
write_file("views.py", f'''    
from django.shortcuts import render    
def home(request):    
    num1 = 5    
    fact1 = fact(num1)    
    return render(request, '{app_name}/index.html', {{'param1': fact1}})      

def fact(num1):    
    result = num1    
    for i in range(result-1, 0, -1):    
        result = result * i    
    return result    
''')
```


## 10. Writing app1/urls.py    
```
write_file("urls.py", f'''    
from django.urls import path    
from {app_name}.views import home    
urlpatterns = [path('', home)]    
''')
```

Please run the following command in terminal:    
$ ***python automation1.py***   

