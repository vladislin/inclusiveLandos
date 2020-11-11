from django.shortcuts import render
from .models import News, Speaker


def home(request):
    return render(request, 'home/index.html', {'news': News.objects.all(),
                                               'speakers': Speaker.objects.all()})
