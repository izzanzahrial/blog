from django.contrib import admin
from .models import BlogPost, Category, Comment

# Register your models here.
@admin.register(BlogPost)
class Admin(admin.ModelAdmin):
    list_display = ('title', 'status', 'category')
    prepopulated_fields = {'slug':('title',),}

@admin.register(Comment)
class Admin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'publish', 'status')
    list_filter = ('status', 'publish')
    search_fields = ('name', 'email', 'content')

admin.site.register(Category)