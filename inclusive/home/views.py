from django.shortcuts import render
from .forms import FeedbackForm, SignupForm
from .models import News, Speaker, SectionOff, Feedback


def home(request):
    feedback_form = FeedbackForm()
    signup_form = SignupForm()
    if request.method == 'POST':
        feedback_form = FeedbackForm(data=request.POST)
        signup_form = SignupForm(data=request.POST)


    if 'feedback_form' in request.POST:
        if feedback_form.is_valid():
            feedback_form.save()
        else:
            feedback_form = FeedbackForm()

    if 'signup_form' in request.POST:
        if signup_form.is_valid():
            signup_form.save()
        else:
            signup_form = SignupForm()


    news = News.objects.all()
    speakers = Speaker.objects.all()
    sections = SectionOff.objects.all()
    ctx = {'feedback_form': feedback_form, 'signup_form': signup_form, 'news': news, 'speakers': speakers, 'sections': sections}
    return render(request, 'home/index.html', ctx)
