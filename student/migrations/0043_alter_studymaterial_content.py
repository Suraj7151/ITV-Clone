# Generated by Django 5.0.6 on 2024-06-08 17:56

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0042_alter_studymaterial_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studymaterial',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]