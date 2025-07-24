import subprocess
import os 

def exec_command(command):
    subprocess.run(command.split(" "), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

def write_file(fname, content):
    f1=open(fname, "w")
    f1.write(content)
    f1.close()

project_name = input("Enter Project Name: ")
app_name = input("Enter App Name: ")
exec_command(f"django-admin startproject {project_name}")
os.chdir(project_name)
exec_command(f"django-admin startapp {app_name}")
os.chdir(project_name)

write_file("settings.py", f'''
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-x-=1=rbbc2&w(-32$k@t#a%tdv1z39$&5vp^$l=978cn^hi2zd'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '{app_name}'
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = '{project_name}.urls'
TEMPLATES = [
    {{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {{
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        }},
    }},
]
WSGI_APPLICATION = '{project_name}.wsgi.application'
DATABASES = {{
    'default': {{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }}
}}
AUTH_PASSWORD_VALIDATORS = [
    {{
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    }},
    {{
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    }},
    {{
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    }},
    {{
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    }},
]
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
''')

write_file("urls.py", f'''
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('{app_name}/', include('{app_name}.urls')),
]
''')

os.chdir(f"../{app_name}")
os.mkdir("templates")
os.chdir("templates")
os.mkdir(app_name)
os.chdir(app_name)

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

write_file("urls.py", f'''
from django.urls import path
from {app_name}.views import home
urlpatterns = [path('', home)]
''')