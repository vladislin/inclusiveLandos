from django.shortcuts import render
from .forms import FeedbackForm, SignupForm
from .models import News, Speaker, Section, Feedback, Recipient
from django.core.mail import send_mail


def home(request):
    emails = list(Recipient.objects.values_list('email', flat=True))
    feedback_form = FeedbackForm()
    signup_form = SignupForm()
    if request.method == 'POST':
        feedback_form = FeedbackForm(data=request.POST)
        signup_form = SignupForm(data=request.POST)

    if 'feedback_form' in request.POST:
        if feedback_form.is_valid():
            username = feedback_form.cleaned_data
            description = feedback_form.cleaned_data
            subject = 'НОВИЙ ФІДБЕК'
            message = 'Ви отримали новий фідбек від {}.\n'\
                      '{}'.format(username['username'], description['description'])
            recipients = emails
            send_mail(subject, message, 'vlad.slinchuk@gmail.com', recipients)
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
    speaker_section = Section.objects.get(pk=3)
    live_section = Section.objects.get(pk=1)
    ctx = {'feedback_form': feedback_form, 'signup_form': signup_form, 'news': news, 'speakers': speakers,
           'speaker_section': speaker_section, 'live_section': live_section}
    return render(request, 'home/index.html', ctx)
