from django.contrib import admin

from .models import Project, Skill, Experience, Study, Recommendation, Presentation


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin) :
    list_display = ['name', 'description', 'status']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'advancement', 'color']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'description']


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'description', 'inline']


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'firstname', 'date', 'message', 'verified']

    # Empêche d'ajouter manuellement des recommandations
    # def has_add_permission(self, request, obj=None):
    #     return False

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ['text']