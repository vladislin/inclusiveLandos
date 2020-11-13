from django.forms import ModelForm
from .models import Feedback, Singup


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'


class SignupForm(ModelForm):
    class Meta:
        model = Singup
        fields = '__all__'
