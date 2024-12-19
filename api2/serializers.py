
from django.contrib.auth.models import User
from blog.models import Category, Comment, Post, Tag
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #fields = '__all__'
        fields = ['id', 'title', 'image', 'like', 'category']

class PostRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #fields = '__all__'
        exclude = ['create_dt']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #fields = '__all__'
        fields = ['like']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class CatetagSerializer(serializers.Serializer):
    cateList = CategorySerializer(many = True)
    tagList = TagSerializer(many = True)