from rest_framework import serializers
from accounts.models import Profile


class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = Profile
        fields = ("id", "first_name", "last_name", "email", "bio", "avatar")
        image = serializers.ImageField(max_length=255, allow_empty_file=True)