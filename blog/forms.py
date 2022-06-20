from django import forms
from django.forms import fields, widgets
from .models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'title_tag', 'body', 'category']
        widgets = {
            "title": forms.TextInput(attrs={"class": ""}),
            "title_tag": forms.TextInput(attrs={"class": ""}),
            "body": forms.Textarea(attrs={"class": ""}),
            "category": forms.TextInput(attrs={"class": ""}),
            "image": forms.ImageField()
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            "name": forms.TextInput(attrs={"class": "col-sm-12 mb-3"}),
            "email": forms.EmailInput(attrs={"class": "col-sm-12 mb-3"}),
            "body": forms.Textarea(attrs={"class": "form-control mb-3"}),
        }

class PostSearchForm(forms.Form):
    q = forms.CharField()