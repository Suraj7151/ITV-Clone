# Generated by Django 5.0.6 on 2024-05-30 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0034_alter_openings_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.DeleteModel(
            name='opening',
        ),
        migrations.RemoveField(
            model_name='subtopic',
            name='topic',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='emergency',
            new_name='contact',
        ),
        migrations.RemoveField(
            model_name='interview',
            name='date',
        ),
        migrations.RemoveField(
            model_name='interviewquestions',
            name='que',
        ),
        migrations.AddField(
            model_name='interview',
            name='link',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='interviewquestions',
            name='ques',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='SubTopic',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
