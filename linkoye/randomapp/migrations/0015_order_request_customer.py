# Generated by Django 4.0.4 on 2023-02-06 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('randomapp', '0014_remove_order_request_customer_order_details_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_request',
            name='Customer',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
