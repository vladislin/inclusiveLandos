from django.contrib import admin
from .models import News, Speaker, Section, Feedback, Singup, Recipient


# class NewsAdmin(admin.ModelAdmin):
#     list_display = ['title', 'description', 'image', 'is_hidden', 'date', 'alt']
#     list_filter = ['date']
#
#
# admin.site.register(News, NewsAdmin)


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'alt', 'description', 'image', 'fb', 'linkedin']
    list_display_links = ['name', 'image', 'fb', 'linkedin']


admin.site.register(Speaker, SpeakerAdmin)


class SectionAdmin(admin.ModelAdmin):
    list_display = ['section_name', 'is_hidden', 'id']


admin.site.register(Section, SectionAdmin)


# class FeedbackAdmin(admin.ModelAdmin):
#     list_display = ['username', 'description']
#
#     class Meta:
#         model = Feedback
#
#
# admin.site.register(Feedback, FeedbackAdmin)


# class RecipientAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email']
#
#
# admin.site.register(Recipient, RecipientAdmin)

# class SingupAdmin(admin.ModelAdmin):
#     list_display = ['name', 'surname', 'phone', 'email', 'description']
#
#     class Meta:
#         model = Singup
#
#
# admin.site.register(Singup, SingupAdmin)
