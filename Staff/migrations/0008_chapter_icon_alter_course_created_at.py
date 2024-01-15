# Generated by Django 4.2.6 on 2023-12-11 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0007_skills_chapter_alter_course_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='icon',
            field=models.ImageField(null=True, upload_to='Chapter_Icons'),
        ),
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.TimeField(default=datetime.datetime(2023, 12, 11, 15, 47, 28, 529586, tzinfo=datetime.timezone.utc)),
        ),
    ]
