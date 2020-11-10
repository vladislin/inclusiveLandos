from django.shortcuts import render
from django.views.generic import ListView
from .models import News


# Create your views here.


class ShowNewsView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

