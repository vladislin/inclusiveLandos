from django.contrib import admin
from .models import News, Speaker, SectionOff, Feedback, Singup


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'is_hidden', 'date', 'alt']
    list_filter = ['date']


admin.site.register(News, NewsAdmin)


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'alt', 'description', 'image', 'fb', 'linkedin']
    list_display_links = ['name', 'image', 'fb', 'linkedin']


admin.site.register(Speaker, SpeakerAdmin)


class SectionOffAdmin(admin.ModelAdmin):
    list_display = ['section_name', 'is_hidden']


admin.site.register(SectionOff, SectionOffAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['username', 'description']

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)


class SingupAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'email', 'description']

    class Meta:
        model = Singup


admin.site.register(Singup, SingupAdmin)
