from django.db import models
class A(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    age = models.IntegerField()
    

# Create your models here.
