from django import forms
from django.forms import fields, widgets
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'title_tag', 'body', 'category']
        widgets = {
            "title": forms.TextInput(attrs={"class": ""}),
            "title_tag": forms.TextInput(attrs={"class": ""}),
            "body": forms.Textarea(attrs={"class": ""}),
            "category": forms.TextInput(attrs={"class": ""}),
        }