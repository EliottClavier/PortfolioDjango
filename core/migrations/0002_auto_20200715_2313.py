# Generated by Django 3.0.8 on 2020-07-15 21:13

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='skills',
        ),
        migrations.AddField(
            model_name='project',
            name='skill_1',
            field=models.ManyToManyField(blank=True, related_name='skill_1', to='core.Skill'),
        ),
        migrations.AddField(
            model_name='project',
            name='skill_2',
            field=models.ManyToManyField(blank=True, related_name='skill_2', to='core.Skill'),
        ),
        migrations.AddField(
            model_name='project',
            name='skill_3',
            field=models.ManyToManyField(blank=True, related_name='skill_3', to='core.Skill'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(help_text='Description du projet'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(help_text='Nom du projet', max_length=150),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.BooleanField(help_text='Hors ligne / En ligne'),
        ),
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, help_text='URL vers le projet', max_length=300),
        ),
        migrations.AlterField(
            model_name='skill',
            name='advancement',
            field=models.IntegerField(help_text='Progression de la compétence'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFF', help_text='Couleur associée à la compétence', max_length=18),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(help_text='Nom de la compétence', max_length=50),
        ),
    ]
