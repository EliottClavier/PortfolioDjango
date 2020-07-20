from django.db import models
from colorfield.fields import ColorField


class Project(models.Model):
    name = models.CharField(max_length=150, help_text="Nom du projet")
    description = models.TextField(help_text="Description du projet")
    url = models.URLField(max_length=300, blank=True, help_text="URL vers le projet")
    image = models.ImageField(upload_to='images/')
    status = models.BooleanField(help_text="Hors ligne / En ligne")
    skill_1 = models.ManyToManyField('Skill', related_name="skill_1", blank=True)
    skill_2 = models.ManyToManyField('Skill', related_name="skill_2", blank=True)
    skill_3 = models.ManyToManyField('Skill', related_name="skill_3", blank=True)


class Skill(models.Model):

    CATEGORIES = [
        ('L', 'language'),
        ('T', 'tool')
    ]

    name = models.CharField(max_length=50, help_text="Nom de la compétence")
    advancement = models.IntegerField(help_text="Progression de la compétence")
    color = ColorField(help_text="Couleur associée à la compétence")
    category = models.CharField(max_length=20, choices=CATEGORIES)

    # Son nom s'affichera lors de la création / édition d'un projet au niveau de la sélection des compétences liées
    def __str__(self):
        return self.name


class Experience(models.Model):
    name = models.CharField(max_length=200, help_text="Nom de l'expérience")
    description = models.TextField(help_text="Description de l'expérience")
    duration = models.CharField(max_length=30, help_text="Durée de l'expérience")


class Study(models.Model):
    name = models.CharField(max_length=200, help_text="Nom de la formation")
    description = models.TextField(help_text="Description de la formation")
    duration = models.CharField(max_length=30, help_text="Durée de la formation")


class Recommendation(models.Model):
    firstname = models.CharField(max_length=50, help_text="Prénom")
    lastname = models.CharField(max_length=50, help_text="Nom")
    companyname = models.CharField(max_length=100, help_text="Nom de l'entreprise", blank=True)
    mail = models.CharField(max_length=100, help_text="Email", blank=True)
    message = models.TextField(help_text="Message de recommandation")
    date = models.DateField(help_text="Date du message")
    verified = models.BooleanField(help_text="Non affichée / Affichée")
