from rest_framework import serializers

from comments.models import Comment

class CommentSerializer(serializers.Serializer):


    class Meta:
        model = Comment
        fields = ['id', 'content', 'post', 'user']