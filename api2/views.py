from django.contrib.auth.models import User
from django.shortcuts import render
from api2.serializers import PostSerializer, UserSerializer
from blog.models import Post
from rest_framework import viewsets

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer