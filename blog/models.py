from django.db import models
from django.db.models.base import Model
from django.urls import reverse

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')

    def __str__(self):
        return self.title + '|' + self.post_date

    def get_absolute_url(self):
        return reverse("home")

    class Meta:
        ordering = ["post_date"]

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")
    
    