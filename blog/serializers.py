from django.contrib.auth.models import User

from blog.models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username', read_only=True)
    category_name = serializers.ReadOnlyField(source='category.name', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'header_image', 'body', 'snippet', 'post_date',
                  'author', 'author_username', 'category', 'category_name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']

        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True
            }
        }