# Generated by Django 4.2.13 on 2024-06-21 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0063_rename_modulename_interviewquestions_modulename'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InterviewQuestions',
        ),
    ]
