# Generated by Django 5.0.6 on 2024-06-10 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0052_alter_profile_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('details', models.TextField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'courseCategories',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=100, null=True)),
                ('details', models.CharField(max_length=100, null=True)),
                ('date', models.DateField()),
                
            ],
            options={
                'db_table': 'course',
            },
        ),
    ]