# Generated by Django 5.0.6 on 2024-06-03 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0035_remove_article_tags_delete_opening_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
