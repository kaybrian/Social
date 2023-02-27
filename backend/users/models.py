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
    is_staff = models.BooleanField(default=False) # a admin user; non super-user

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'name']


    def get_full_name(self):
        # The user is identified by their email address
        return self.name

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    


