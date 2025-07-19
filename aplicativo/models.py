from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.

class Item(models.Model):
    name=models.CharField()
    category_id=models.IntegerField()
    
class Category(models.Model):
    ct_name=models.CharField()
    ct_id=models.IntegerField()

class User(models.Model):
    username=models.CharField()
    password=models.CharField()
    email=models.EmailField()
    first_name=models.CharField()
    last_name=models.CharField()
   


