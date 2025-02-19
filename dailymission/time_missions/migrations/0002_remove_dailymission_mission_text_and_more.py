# Generated by Django 5.1.2 on 2024-10-28 14:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_missions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailymission',
            name='mission_text',
        ),
        migrations.AddField(
            model_name='dailymission',
            name='description',
            field=models.CharField(default='기본 설명', max_length=255),
        ),
        migrations.AddField(
            model_name='dailymission',
            name='title',
            field=models.CharField(default='기본 제목', max_length=255),
        ),
        migrations.AlterField(
            model_name='dailymission',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
