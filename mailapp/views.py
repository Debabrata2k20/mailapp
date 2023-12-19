from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, template_name="home.html")


def send(request):
    x = request.GET['fn']
    y = request.GET['ln']
    z = request.GET['em']
    From_mail = settings.EMAIL_HOST_USER
    to_list = [z]
    msg = "Hi "+ x + " " + y +". Thanks for contacting us !!"
    subject = "Thank You"
    send_mail(subject,msg,From_mail,to_list,fail_silently=False)
    return HttpResponse("Please,Check your mail !")