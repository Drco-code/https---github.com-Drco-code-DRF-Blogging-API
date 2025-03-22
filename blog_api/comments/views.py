from django.shortcuts import render

from rest_framework import generics

from comments.models import Comment
from comments.serializers import CommentSerializer

# Create your views here.

class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment
    serializer_class = CommentSerializer
