from django.contrib import admin
from .models import News

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'date', 'alt']
    list_filter = ['date']

admin.site.register(News, NewsAdmin)