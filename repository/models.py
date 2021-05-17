from django import urls
from django.db import models
from django.urls import reverse

# Create your models here.
class Repository(models.Model):
    repo_id = models.IntegerField(primary_key=True, max_length=255, unique=True)
    repo_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    created_date = models.DateField()

    def __str__(self):
        return self.repo_name + '|' + self.created_date
    
    def get_absolute_url(self):
        return reverse("home")

    class Meta:
        ordering = ["created_date"]
    
