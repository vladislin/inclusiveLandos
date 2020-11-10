from django.contrib import admin
from .models import Speaker


# Register your models here.

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'alt', 'description', 'image', 'fb', 'linkedin']
    list_display_links = ['fb', 'linkedin']


admin.site.register(Speaker, SpeakerAdmin)
