from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, name, email, date_of_birth, password=None, **extra_fields):
        if not email:
            raise ValueError("A user must have an email")

        email = self.normalize_email(email)
        user = self.model(
            name=name,
            email=email,
            date_of_birth=date_of_birth,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, date_of_birth, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        user = self.create_user(
            name,
            email,
            date_of_birth,
            password,
            **extra_fields
        )
        user.save(using=self._db)
        return user
