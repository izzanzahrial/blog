from django.contrib import admin
from .models import BlogPost, Category

# Register your models here.
@admin.register(BlogPost)
class Admin(admin.ModelAdmin):
    list_display = ('title', 'category')
    #prepopulated_fields = {"slug": ("title")}

admin.site.register(Category)