from django.db import models
from users.models import CustomUser
from cloudinary.models import CloudinaryField
from django.urls import reverse
import uuid
from django.template.defaultfilters import slugify



class Post(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = CloudinaryField('image',blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    likes = models.ManyToManyField(CustomUser, related_name='blogpost_like')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def image_url(self):
        if self.image:
            return (
                f"http://res.cloudinary.com/ctrl-uganda/{self.image}"
            )
        return ""


    def number_of_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return str(self.unique_id)

