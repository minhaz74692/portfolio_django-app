from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.IntegerField()
    userName  = models.CharField(max_length= 24)
    email = models.CharField(max_length=30)
    age  = models.IntegerField()
    profession = models.CharField(max_length= 20)