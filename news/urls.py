from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('news/', views.ShowNewsView.as_view(), name='news'),
]