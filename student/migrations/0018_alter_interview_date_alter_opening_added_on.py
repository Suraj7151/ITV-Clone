# Generated by Django 5.0.6 on 2024-05-29 07:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_alter_interview_date_alter_opening_added_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 29, 7, 45, 53, 291672, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='opening',
            name='added_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 29, 7, 45, 53, 291672, tzinfo=datetime.timezone.utc)),
        ),
    ]
