from rest_framework import serializers


from likes.models import LikeDislike


class LikeDislike(serializers.Serializer):

    class Meta:
        model = LikeDislike
        fields = ['id', 'type', 'post', 'user']