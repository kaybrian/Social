from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, name, email, date_of_birth, password=None):
        if not email:
            raise ValueError("A user must have an email")

        email = self.normalize_email(email)
        user = self.model(
            name=name,
            email=email,
            date_of_birth=date_of_birth
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, date_of_birth, password=None):
        user = self.create_user(
            email,
            name=name,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
