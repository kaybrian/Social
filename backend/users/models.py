from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import MyUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name= models.CharField(max_length=150)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'name']


    def __str__(self):
        return self.email


    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name



