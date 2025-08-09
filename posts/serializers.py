# posts/serializers.py
from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = {
            'slug': {'required': False},
            'author': {'required': False}
        }

    def validate_title(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("عنوان باید حداقل ۱۰ کاراکتر باشد")
        return value