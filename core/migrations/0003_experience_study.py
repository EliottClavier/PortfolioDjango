# Generated by Django 3.0.8 on 2020-07-18 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200715_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Nom de l'expérience", max_length=200)),
                ('description', models.TextField(help_text="Description de l'expérience")),
                ('duration', models.CharField(help_text="Durée de l'expérience", max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nom de la formation', max_length=200)),
                ('description', models.TextField(help_text='Description de la formation')),
                ('duration', models.CharField(help_text='Durée de la formation', max_length=30)),
            ],
        ),
    ]