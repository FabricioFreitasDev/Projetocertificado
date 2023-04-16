# Generated by Django 4.2 on 2023-04-15 12:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0002_evento_participantes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='participantes',
            field=models.ManyToManyField(blank=True, null=True, related_name='evento_participantes', to=settings.AUTH_USER_MODEL),
        ),
    ]
