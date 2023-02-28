from django.db import models
from users.models import CustomUser
from cloudinary.models import CloudinaryField
from django.urls import reverse
import uuid
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_delete
import cloudinary
from django.dispatch import receiver



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


class Comment(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField()
    likes = models.ManyToManyField(CustomUser, related_name='comment_like')
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def number_of_likes(self):
        return self.likes.count()


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Comment on post by {self.user.name}'





# delete the image from Cloundinary whenever the post is deleted
@receiver(pre_delete, sender=Post)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)
