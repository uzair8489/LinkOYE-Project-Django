# Generated by Django 4.0.4 on 2023-04-02 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomapp', '0026_bankdetails_ach_routing_bankdetails_currency_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankdetails',
            name='ACH_Routing',
        ),
        migrations.AddField(
            model_name='bankdetails',
            name='File',
            field=models.FileField(default='', upload_to='Bank Detail'),
            preserve_default=False,
        ),
    ]
