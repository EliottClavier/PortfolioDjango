from django.shortcuts import render

from .models import Project, Skill, Experience, Study, Recommendation


def homepage(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    studies = Study.objects.all()
    return render(request, 'core/homepage.html', {
        'projects': projects,
        'skills': skills,
        'experiences': experiences,
        'studies': studies,
    })


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
