# Generated by Django 3.2.20 on 2023-12-06 12:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth_module', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='school',
        ),
        migrations.RemoveField(
            model_name='teacherprofile',
            name='school',
        ),
        migrations.AddField(
            model_name='school',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='schools', to=settings.AUTH_USER_MODEL),
        ),
    ]
