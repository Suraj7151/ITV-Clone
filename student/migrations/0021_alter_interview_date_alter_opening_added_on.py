# Generated by Django 5.0.6 on 2024-05-29 08:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0020_remove_profile_user_alter_interview_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 29, 8, 7, 50, 294021, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='opening',
            name='added_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 29, 8, 7, 50, 294021, tzinfo=datetime.timezone.utc)),
        ),
    ]
