from django.shortcuts import render
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from .models import BlogPost, Category
from .serializer import BlogPostSerializer, CategorySerializer

# Create your views here.
class BlogPostViewSet(viewsets.ViewSet):
    def list(self, request):
        blogPosts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blogPosts, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BlogPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        blogPost = BlogPost.objects.get(id=pk)
        serializer = BlogPostSerializer(blogPost)
        return Response(serializer.data)

    def update(self, request, pk=None):
        blogPost = BlogPost.objects.get(id=pk)
        serializer = BlogPostSerializer(instance=blogPost, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        blogPost = BlogPost.objects.get(id=pk)
        blogPost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def update(self, request, pk=None):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(instance=category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        category = Category.objects.get(id=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)