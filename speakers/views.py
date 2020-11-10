from django.views.generic import ListView
from .models import Speaker


# Create your views here.


class ShowSpeakersView(ListView):
    model = Speaker
    template_name = 'speakers/inner.html'
    context_object_name = 'speakers'
