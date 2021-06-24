from django.contrib import admin

# Register your models here.

from .models import Login #relative Import


admin.site.register(Login)



