"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import BlogPostViewSet, CategoryViewSet, BlogPostsView, PostDetailView, CreatePostView #BlogPostView, BlogPostDetailView,

app_name = 'blog'

urlpatterns = [
    path('api/', BlogPostViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',
        }
    )),
    path('api/<str:pk>', BlogPostViewSet.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy',
        }
    )),
    path('category/api', CategoryViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',
        }
    )),
    path('category/api/<str:pk>', CategoryViewSet.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy',
        }
    )),
    # path('/', BlogPostView.as_view(),),
    # path('/<str:pk>', BlogPostDetailView.as_view(), name="post-detail"),
    path('', BlogPostsView, name="blog-posts"),

    path('<slug:post>', PostDetailView, name="post-detail"),

    path('create/', CreatePostView, name="create-post"),
]
