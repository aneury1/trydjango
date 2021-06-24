from django.db import models

# Create your models here.
class Login(models.Model):
    name     = models.CharField(max_length=123)
    password = models.TextField()
    email    = models.TextField()
    token    = models.TextField(default="no token - provide for this")