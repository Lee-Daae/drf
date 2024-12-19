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

from api2.serializers import CatetagSerializer, CommentSerializer, PostLikeSerializer, PostListSerializer, PostRetrieveSerializer
from blog.models import Category, Comment, Post, Tag
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# patch 메소드 구현, UpdateAPIView는 put과 patch 만 가능
class PostLikeAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostLikeSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        # data = instance.like + 1 딕셔너리가 아니라 숫자만 나오게 하려고 하면 drf serializer : dict-like 기반이라 오류나서 response 바꿔야 됨
        data = {'like': instance.like + 1}
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        #return Response(serializer.data)
        return Response(data['like'])
    
class CateTagAPIView(APIView):
    # Cannot apply DjangoModelPermissionsOrAnonReadOnly on a view that does not set `.queryset` or have a `.get_queryset()` method.
    def get_queryset(self):
        return Category.objects.all()

    def get(self, request, *args, **kwargs):
        cateList = Category.objects.all()
        tagList = Tag.objects.all()
        data = {
            'cateList' : cateList,
            'tagList' : tagList,
        }
        serializer = CatetagSerializer(instance=data)
        return Response(serializer.data)