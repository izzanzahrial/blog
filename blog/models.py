from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class BlogPost(models.Model):

    title = models.CharField(max_length=255, unique=True)
    title_tag = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=False)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')

    def __str__(self):
        return self.title + '|' + str(self.post_date)

    def get_absolute_url(self):
        return reverse("blog:post-detail", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["-post_date"]

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    