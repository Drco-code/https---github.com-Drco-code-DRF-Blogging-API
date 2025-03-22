from django.shortcuts import render

from rest_framework import generics

from blog.models import BlogPost
from blog.serializers import BlogPostSerializer

# Create your views here.


class BlogPostListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogPost
    serializer_class = BlogPostSerializer
