# Generated by Django 4.2.6 on 2024-01-09 12:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Staff', '0011_alter_course_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.TimeField(default=datetime.datetime(2024, 1, 9, 12, 27, 49, 189138, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='course',
            name='paid_user',
            field=models.ManyToManyField(blank=True, null=True, related_name='paid_course', to=settings.AUTH_USER_MODEL),
        ),
    ]
