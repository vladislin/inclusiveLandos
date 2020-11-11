from django.contrib import admin
from .models import News, Speaker


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'is_hidden', 'date', 'alt']
    list_filter = ['date']


admin.site.register(News, NewsAdmin)


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'alt', 'description', 'image', 'fb', 'linkedin']
    list_display_links = ['fb', 'linkedin']


admin.site.register(Speaker, SpeakerAdmin)
