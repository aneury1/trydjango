# TryDjango 

this is the first time I try Django Project or maybe not but now I'm try to get the basic concepts that are need to setup
great webapps using Django maybe as backend services.

firtst I'm going to try to use this as placeholder; for other projects.

## Start new Project
django-admin startproject <ProjectName>


## Run Server
python manage.py runserver

## Syncs Setting for Database 
we are going to use any kind of supported db therefore with need to sync before anything else
for this we would use *python manage.py migrate* this will do the trick.

## Admin Panel
to access the admin panel go to host url with end point /admin, in case you did not have the user and password is maybe because i did not setup the super user, for this what you can do is run in the 
terminal the next command *python manage.py createsuperuser* this will prompt for username,email,and password and passwordconfirmation and thats it.

## Application components.
these components allow us to customize and are the heart of our application so, is good idea to 
start with, where should I setup my applications' components, in Django application go to 
settings.py and look for INSTALLED_APPS, you would see that by default some are installed already
this array has: Admin, Auth, ContentTypes, sessions, messages,staticfiles. these names are so
self descriptives so we could ignore by now, by the way here you would add your owns application components and third party components as well.

to create new application components fro django go to the command line in the manage.py location
and use *python manage.py startapp <AppName>* where AppName is the name of the app component you want to create.

### Application Components Model
when you create new application component, maybe you would need to create a new model(s) for this component if so you can go to the models file inside the folder of your app, the there create a new class that inherits from models.Model this class would have some attributes that would be use as columns on the tables of your models in database. for example.
```
   from django.db import models
   class User(models.Model):
        id        = models.TextField()
        name      = models.CharField(max_length=64)
        email     = models.CharField(max_length=64)
        password  = models.CharField(max_length=64)
        summary   = models.TextField()
        status    = models.TextField(default="not avilable")
```

this would create the, but one step is necesary to update the migration for this class, go to terminal and the setting the terminal in 
the directory of your manage.py run *python manage.py makemigrate* with this command you flag the migrate that some migration is pending, 
something I forgot to mention is after the creation of your app component you need to "Install"
the component to do that go to *setting.py* then add this to  *INSTALLED_APPS* array and then run the above command 
to flag the migration this will do the trick. pd: every time you update your model run makemigrations and the migrate


### Work with Model in the Admin Panel

go the **AppComponent**/admin.py folder import the class from models.py in the same folder
then use ```admin.site.register(CLASS_IMPORTED)```from it, if you want to see the change
go to /admin endpoint and you should see the entry options with the model you have created
in pluralize form, you would have some options that the labels for me where self explanatory. 


### work with Python shell inside my project

go to the root of you project and run ```python manage.py shell```, an example of usage are shown bellow:
```
Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from login.models import Login
>>> Login.objects.all()
<QuerySet [<Login: Login object (1)>]>
>>> Login.objects.create(name='aneury', password='1234dffdf', email='aneury1@df', token='123454fdfdfffffdfdfsfsdfsdf')
<Login: Login object (2)>
>>> Login.objects.all()
<QuerySet [<Login: Login object (1)>, <Login: Login object (2)>]>
```
this is the way to create a retrieve object and create object in the shell
other thing is the Fields types are well documented on the official site please visit there for more references.

## Add, Update routes

first use existing application component ocreate new one, 
remeber ```python manage.py startapp <APPCMPname>``` open the view on the new component/existing component.

to create a endpoint function follow the next snipped in view.py and url.py
```
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page_view(*args, **kwargs):
    return HttpResponse("<h1>Hi, there</h1>")

def login_view(request, *args, **kwargs):
    print(request.user)
    return HttpResponse('<input type="text" placeholder="add your name" />')
```
and url.py
```
from django.contrib import admin
from django.urls import path

from page import views

urlpatterns = [
    path('', views.page_view, name='page'),
    path('admin/', admin.site.urls),
]
```
as you can see you can have many function to map specific endpoint in the application so it depends on you,by default your function will have request object that has some properties you maybe mention later in this document.


## Adding templates files
now that we see how to add routes is good idea to render on the client side something more interesting that simple html lines, we can do it better by using Template mechanism that are built-in on django to do so, first we can create new folder at project level by recomendation, where templates will live, then add this path to the settings.py, go in the ```TEMPLATE``` array look for the attributes ```DIRS``` which is an array and the path of your project, one common approach you could is use import os from and use:
```
   import os
   ...
   BASE_DIR = ...
   ...
   DIRS:[os.path.join(BASE_DIR, 'template')]
   ... 
```
after this done you could go to the function where you want to render a template and do something similar than: 
```Note that index.html``` **must** reside within templates folder:
```
def login_view(request, *args, **kwargs):
    return render(request, 'login.html')
```



