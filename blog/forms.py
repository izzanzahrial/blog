from django import forms
from django.forms import fields
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'title_tag', 'body', 'category']
        