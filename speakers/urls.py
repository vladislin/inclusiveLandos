from django.urls import path
from . import views

urlpatterns = [
    path('speakers/', views.ShowSpeakersView.as_view(), name='speakers'),
]