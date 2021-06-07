from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

def media_update(instance, filename):
    return f'posts/{instance.id}/{filename}'

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class BlogPost(models.Model):

    class Published(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    status_options = (('draft', 'Draft'), ('published', 'Published'))

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=255, unique=True, verbose_name='title')
    title_tag = models.CharField(max_length=255, verbose_name='title tag')
    slug = models.SlugField(max_length=255, null=False)
    image = models.ImageField(upload_to='posts/', blank=True)
    body = models.TextField(verbose_name='content')
    post_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=status_options, default='draft')
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=None)
    objects = models.Manager()
    publiished = Published() #custom manager

    def __str__(self):
        return self.title + ' | ' + str(self.post_date)

    def get_absolute_url(self):
        return reverse("blog:post", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["-post_date"]

class Comment(models.Model):

    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ["publish"]

    def __str__(self):
        return f"Comment by {self.name}"