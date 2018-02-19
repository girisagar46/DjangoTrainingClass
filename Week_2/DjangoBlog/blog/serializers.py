from django.utils import timezone
from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('pk', 'author', 'title', 'text', 'slug')
