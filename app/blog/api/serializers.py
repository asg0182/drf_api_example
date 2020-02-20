

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from rest_framework import serializers, exceptions
from blog.models import Post


User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(required=True)

    class Meta:
        model = Post
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        try:
            username = validated_data.pop('author')
            author = User.objects.get(username=username)
            validated_data['author'] = author
            return Post.objects.create(**validated_data)
        except ObjectDoesNotExist:
            raise exceptions.ParseError
