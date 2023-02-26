from django.db import models
from users.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = PhoneNumberField(blank=True)
    sex = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male',blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    Profession = models.CharField(max_length=350, null=True, blank=True)

    def __str__(self):
        return self.phone_number



