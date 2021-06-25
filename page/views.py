from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hi, there</h1>")

def create_fake_job(name):
    return {
        "name":name,
        "description":'new jobs for this listing',
        "time":1234
    }


# Create your views here.
def login_view(request, *args, **kwargs):
    return render(request, 'login.html')

def conf_view(request, *args, **kwargs):
    return render(request, 'configuration.html')

def jobs_view(request, *args, **kwargs):
    array=[1,'343434','@text',{'1221':1233}]
    single_value=10011  
    str='this is a string'
    my_context ={
            'array': array,
            'single_value': single_value,
            'string': str
        }
    return render(request, 'jobs.html', my_context)

def signup_view(request, *args, **kwargs):
    return render(request, 'registry.html')

