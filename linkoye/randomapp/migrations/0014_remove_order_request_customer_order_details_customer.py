# Generated by Django 4.0.4 on 2023-02-06 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('randomapp', '0013_remove_order_request_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_request',
            name='Customer',
        ),
        migrations.AddField(
            model_name='order_details',
            name='Customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
