from django.contrib import admin
from .models import BlogPost, Category

# Register your models here.
class Admin(admin.ModelAdmin):
    list_display = ('title', 'category')
    prepopulated_fields = {"slug": ("title")}

admin.site.register(BlogPost)
admin.site.register(Category)