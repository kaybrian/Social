from rest_framework import serializers
from .models import Profile
from users.models import CustomUser
from phonenumber_field.serializerfields import PhoneNumberField




class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'date_of_birth')


class ProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    phone_number =PhoneNumberField()
    image_url = serializers.ReadOnlyField()
    class Meta:
        model = Profile
        fields = ('id', 'user', 'email','phone_number','sex','location','Profession', 'image_url','profile_image')

        def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation.pop("profile_image")

            return representation

class UpdateProfile(serializers.ModelSerializer):
    pass


