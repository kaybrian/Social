from django.db import models
from users.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField



GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    profile_image = CloudinaryField('image')
    email = models.EmailField(max_length=255, unique=True)
    phone_number = PhoneNumberField(blank=True)
    sex = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male',blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    Profession = models.CharField(max_length=350, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateField(auto_now=True)


    @property
    def image_url(self):
        return (
            f"http://res.cloudinary.com/ctrl-uganda/{self.image}"
        )

    def __str__(self):
        return str(self.phone_number)
