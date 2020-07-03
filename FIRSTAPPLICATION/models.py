from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(models.Model):
    CustomID=models.CharField(max_length=20,unique=False)
    Name=models.CharField(max_length=20,unique=False)
    Contact=models.CharField(max_length=20,unique=False)
    Address=models.CharField(max_length=20,unique=False)