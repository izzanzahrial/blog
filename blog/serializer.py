from rest_framework import serializers
from django.utils.text import slugify
from .models import BlogPost, Category

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'title_tag', 'body', 'category', 'slug']
        read_only_fields = ['slug']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'