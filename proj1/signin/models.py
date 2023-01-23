from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
'''
class UserProfileManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email),
                          username=username,
                          )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_staffuser(self, email, username, password=None):
        user = self.create_user(email,
                                password=password,
                                username=username
                                )
        user.is_staff = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email,
                                password=password,
                                username=username
                                )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)

        return user
'''


class User(models.Model):
    Username = models.CharField(max_length=150,
                                unique=True,
                                error_messages={
                                    'unique': "A user with that username already exists.",
                                }, )
    Email = models.EmailField()
    Password = models.TextField()

    USERNAME_FIELD = 'Username'
    REQUIRED_FIELDS = ['email']

