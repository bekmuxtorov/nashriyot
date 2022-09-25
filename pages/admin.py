from django.contrib import admin
from . import models

# Register your models here.

class AdminArticles(admin.ModelAdmin):
    list_display = ['id', 'title', 'date', 'blog_view']
admin.site.register(models.Articles, AdminArticles)