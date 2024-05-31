# Generated by Django 5.0.6 on 2024-05-29 06:36

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_module_link_alter_interview_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='interview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 29, 6, 35, 53, 920831, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='opening',
            name='added_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 29, 6, 35, 53, 920831, tzinfo=datetime.timezone.utc)),
        ),
    ]
