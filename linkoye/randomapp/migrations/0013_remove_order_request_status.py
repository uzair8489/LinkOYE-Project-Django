# Generated by Django 4.0.4 on 2023-02-06 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('randomapp', '0012_alter_order_details_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_request',
            name='Status',
        ),
    ]
