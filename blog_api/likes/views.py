from django.shortcuts import render

from rest_framework import generics

from likes.models import LikeDislike
from likes.serializers import LikeDislikeSerializers

# Create your views here.

class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = LikeDislike
    serializer_class = LikeDislikeSerializers
