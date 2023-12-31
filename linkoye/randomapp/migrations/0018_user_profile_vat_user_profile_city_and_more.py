# Generated by Django 4.0.4 on 2023-02-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomapp', '0017_remove_order_details_completion_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='VAT',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_profile',
            name='city',
            field=models.CharField(default='Lahore', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_profile',
            name='company',
            field=models.CharField(default='Company', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_profile',
            name='country',
            field=models.CharField(default='Pakistan', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_profile',
            name='postal_code',
            field=models.CharField(default='55360', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_profile',
            name='website',
            field=models.CharField(default='www.google.com', max_length=300),
            preserve_default=False,
        ),
    ]
