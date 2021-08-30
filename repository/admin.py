from django.contrib import admin
from .models import Repository

# Register your models here.
@admin.register(Repository)
class Admin(admin.ModelAdmin):
    list_display = ('repo_id', 'repo_name', 'description', 'url', 'created_date')
    list_filter = ('repo_id', 'repo_name', 'created_date')
    search_fields = ('repo_id', 'repo_name', 'url', 'created_date')

