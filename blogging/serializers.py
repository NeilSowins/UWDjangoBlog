from rest_framework import serializers
from blogging.models import Post, Category
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "text",
            "author",
            "created_date",
            "modified_date",
            "published_date",
        ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "description", "posts"]
