from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hi, there</h1>")



# Create your views here.
def login_view(request, *args, **kwargs):
    print(request.user)
    # return HttpResponse('<input type="text" placeholder="add your name" />')
    return render(request, 'login.html')