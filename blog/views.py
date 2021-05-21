from core.settings import URL
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from .models import BlogPost, Category
from .serializer import BlogPostSerializer, CategorySerializer
from .forms import BlogPostForm

import requests

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

def blogPostsView(request):

    all_posts = BlogPost.objects.all()

    return render(request, 'blog_posts.html', {"posts": all_posts})

def postDetailView(request, post=None):
    
    blogDetail = get_object_or_404(BlogPost, slug=post)
    
    return render(request, "post_detail.html", {"post": blogDetail})

def blogPostFormView(request):
    
    #using API
    #URL = "http://host.dokcer.internal:8000/repository/api"

    if request.method == "POST":
        blog_post_form = BlogPostForm(request.POST)

        if blog_post_form.is_valid():
            blog_post = blog_post_form.save()
            return HttpResponseRedirect('/blog/' + blog_post.slug)

        #using API
        # requests.post(url=URL, data=blog_post_form)
        # return HttpResponseRedirect('/blog/')

    else:
        blog_post_form = BlogPostForm()
    
    return render(request, 'create_post.html', {'blog_post_form': blog_post_form})
