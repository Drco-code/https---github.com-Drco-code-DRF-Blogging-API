from django.shortcuts import render

from rest_framework import generics

from accounts.models import Profile
from accounts.serializers import ProfileSerializer

# Create your views here.



class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile
    serializer_class = ProfileSerializer