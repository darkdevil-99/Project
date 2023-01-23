from django.db import models


# Create your models here.

class User1(models.Model):
    Username = models.CharField(max_length=150,
                                unique=True,
                                error_messages={
                                    'unique': "A user with that username already exists.",
                                }, )
    Email = models.EmailField()
    Password = models.TextField()
    Confirm_Password = models.TextField()
    First_name = models.TextField()
    Last_name = models.TextField()
    Token = models.TextField(null=True)







