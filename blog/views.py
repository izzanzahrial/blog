import time
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import paginator
# from core.settings import URL
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from datetime import timedelta, date
from .models import BlogPost, Category, Comment
from .serializer import BlogPostSerializer, CategorySerializer
from .forms import BlogPostForm, CommentForm, PostSearchForm
from .decorator import allowed_users

import requests

# Create your views here.
class BlogPostViewSet(LoginRequiredMixin, viewsets.ViewSet):
    login_url = "/account/login/"
    redirect_field_name = "login"

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

class CategoryViewSet(LoginRequiredMixin, viewsets.ViewSet):
    login_url = "/account/login/"
    redirect_field_name = "login"
    
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

class CategoryListView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'categories'

    def get_queryset(self):
        # posts = BlogPost.objects.filter(category__name= self.kwargs['category'])
        # posts_date = []

        # # turn every post date into range from post created until now
        # for post in posts:
        #     posts_date.append(post_created(post.post_date))

        content = {
            'category': self.kwargs['category'],
            'posts': BlogPost.objects.filter(category__name= self.kwargs['category']),
            # 'posts_date' : posts_date,
            #'posts': BlogPost.objects.filter(category__name= self.kwargs['category']).filter(status='published')
        }
        return content

def blogPostsView(request):

    posts = BlogPost.objects.all().order_by('-id')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    blogposts = paginator.get_page(page_number)
    #published_posts = BlogPost.publiished.all()

    return render(request, 'blog/blogpost.html', {"blogposts": blogposts})

def postDetailView(request, post=None):
    
    post = get_object_or_404(BlogPost, slug=post)
    #blogDetail = get_object_or_404(BlogPost, slug=post, status="published")

    fav = bool
    
    if post.favourites.filter(id=request.user.id).exists():
        fav = True

    comments = Comment.objects.filter(status=True)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect('/blog/' + post.slug)
    else:
        comment_form = CommentForm()
    
    return render(request, "blog/post.html", {"post": post, "comments": comments, "comment_form": comment_form, "fav":fav})

@login_required
@allowed_users(allowed_roles=['admin'])
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
    
    return render(request, 'blog/create.html', {'blog_post_form': blog_post_form})

def category_list(request):
    category_list = Category.objects.all()
    context = {
        "category_list": category_list,
    }
    return context

def post_search(request):
    form = PostSearchForm()
    q = ''
    results = []

    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            results = BlogPost.objects.filter(title__contains=q)
        
    return render(request, 'blog/search.html', {'form': form, 'q':q, 'results':results})

# def post_created(post_date):
#     today = date.today()
#     days1 = (today.year * 365) + (today.month * 30) + today.day
#     days2 = (int(post_date[9:]) *365) + (int(post_date[0:3]) * 30) + int(post_date[5:7])
#     time1 = timedelta(days=days1)
#     time2 = timedelta(days=days2)
#     time = time1 - time2
#     return time.days