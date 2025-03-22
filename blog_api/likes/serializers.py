from rest_framework import serializers


from likes.models import LikeDislike


class LikeDislikeSerializers(serializers.Serializer):

    class Meta:
        model = LikeDislike
        fields = ['id', 'type', 'post', 'user']