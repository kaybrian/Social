from django.dispatch import receiver
from django.db.models.signals import post_save
from users.models import CustomUser
from .models import Profile



@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        Profile.objects.create(
            user=user,
            email = user.email
        )


@receiver(post_save, sender=Profile)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=Profile)
def updateuser(sender,instance,created,**kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.email = profile.email
