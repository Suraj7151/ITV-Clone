# Generated by Django 5.0.6 on 2024-06-09 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0045_delete_studytopic'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'StudyTopic',
            },
        ),
    ]
