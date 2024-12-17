# from django.contrib.auth.models import User
# from django.shortcuts import render
# from api2.serializers import CommentSerializer, PostSerializer, UserSerializer
# from blog.models import Comment, Post
# from rest_framework import viewsets

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

from api2.serializers import CommentSerializer, PostListSerializer, PostRetrieveSerializer
from blog.models import Comment, Post
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
