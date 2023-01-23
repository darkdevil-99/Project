from django.db import models


# Create your models here.

class Table(models.Model):
    username = models.TextField(max_length=20, unique=True)
    email = models.TextField()
    password = models.TextField()





