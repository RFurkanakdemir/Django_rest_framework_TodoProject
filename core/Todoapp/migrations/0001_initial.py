# Generated by Django 4.1.4 on 2022-12-26 14:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(auto_created=True, default='normal Categorie', max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Enter Title', max_length=25)),
                ('priority', models.CharField(choices=[('crucial', 'Crucial'), ('important', 'İmportant'), ('normal', 'Normal'), ('not urgent', 'Not Urgent'), ('unimportant', 'Unimportant')], default='normal', max_length=20)),
                ('content', models.TextField(blank=True, default='Enter Task', max_length=300)),
                ('startingDate', models.DateTimeField(default=datetime.datetime(2022, 12, 26, 17, 35, 51, 853903))),
                ('endDate', models.DateTimeField(blank=True)),
                ('isActive', models.BooleanField(blank=True, default=True)),
                ('categorie', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='Todoapp.categorie')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
