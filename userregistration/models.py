from django.db import models

# Create your models here.

class UserAuthentication(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    datetime = models.DateField(auto_now=True)
    status = models.CharField(max_length=100)