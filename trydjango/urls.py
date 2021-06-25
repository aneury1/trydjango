"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from page.views import page_view
from page.views import login_view
from page.views import conf_view
from page.views import jobs_view
from page.views import signup_view

urlpatterns = [
    path(''        , page_view     , name='page'),
    path('home/'   , page_view     , name='page'),
    path('login/'  , login_view    , name='page'),
    path('jobs/'   , jobs_view     , name='page1'),
    path('signup/' , signup_view   , name='page2'),
    path('conf/'   , conf_view     , name='page3'),

    path('admin/', admin.site.urls),
]
