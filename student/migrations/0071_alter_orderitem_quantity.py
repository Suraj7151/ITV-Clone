# Generated by Django 5.0.6 on 2024-07-02 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0070_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
