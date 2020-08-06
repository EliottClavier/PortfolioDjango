from django.shortcuts import render
from django.http import JsonResponse
from .models import Project, Skill, Experience, Study, Recommendation
from .forms import RecommendationForm, ContactForm

from django.core import mail
import json as simplejson
from datetime import date

def homepage(request):

    projects = Project.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    studies = Study.objects.all()

    contact_form = ContactForm()
    recommendation_form = RecommendationForm()

    return render(request, 'core/homepage.html', {
        'projects': projects,
        'skills': skills,
        'experiences': experiences,
        'studies': studies,
        'recommendationForm': recommendation_form,
        'contactForm': contact_form
    })


def ajax_recommendation(request):
    if request.method == "POST" and request.is_ajax():
        form = RecommendationForm(request.POST)
        if form.is_valid():

            new_recommendation = Recommendation()

            new_recommendation.firstname = form.cleaned_data['firstname']
            new_recommendation.lastname = form.cleaned_data['lastname']
            new_recommendation.companyname = form.cleaned_data['companyname']
            new_recommendation.mail = form.cleaned_data['mail']
            new_recommendation.message = form.cleaned_data['message']
            new_recommendation.date = date.today()
            new_recommendation.verified = False

            new_recommendation.save()
        return JsonResponse({"success": True}, status=200)
    return JsonResponse({"success": False}, status=400)


def ajax_contact(request):
    if request.method == 'POST' and request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['companyName']:
                subject = form.cleaned_data['messageObject'] + " - " + form.cleaned_data['companyName']
            else:
                subject = form.cleaned_data['messageObject']
            plain_message = form.cleaned_data['message']
            from_email = form.cleaned_data['mail']
            to = 'eliott.clavier@students.campus.academy'
            mail.send_mail(subject, plain_message, from_email, [to])
        return JsonResponse({"success": True}, status=200)
    return JsonResponse({"success": False}, status=400)


def projects(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    return render(request, 'core/project.html', {
        'projects': projects,
        'skills': skills
    })


def recommendations(request):
    recommendations = Recommendation.objects.all()
    return render(request, 'core/recommend.html', {
        'recommendations': recommendations
    })
