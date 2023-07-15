# Generated by Django 4.0.4 on 2022-09-14 22:02

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Thumbnail', models.ImageField(upload_to='Service_Thumbnail')),
                ('Blog_Title', models.CharField(max_length=200)),
                ('Author', models.CharField(max_length=200)),
                ('Description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Link_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Link_Type', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Order_Details',
            fields=[
                ('Order_ID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Status', models.CharField(choices=[('completed', 'COMPLETED'), ('to do', 'TO DO')], max_length=20)),
                ('Paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Service_Category_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('URL', models.CharField(max_length=300)),
                ('DA', models.IntegerField()),
                ('PA', models.IntegerField()),
                ('Organic_Traffic', models.IntegerField()),
                ('Link_Allowed', models.IntegerField()),
                ('Link_Type', models.CharField(max_length=200)),
                ('Country', models.CharField(max_length=100)),
                ('Language', models.CharField(max_length=100)),
                ('Image_Allowed', models.IntegerField()),
                ('Description', models.TextField()),
                ('Restricted_Topics', models.TextField()),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=11)),
                ('skype', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Thumbnail', models.ImageField(upload_to='Service_Thumbnail')),
                ('Service_Title', models.CharField(max_length=200)),
                ('Description', models.TextField()),
                ('Service_Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='randomapp.service_category')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('URL', models.CharField(max_length=300)),
                ('Title', models.CharField(max_length=300)),
                ('Order_Date', models.DateField()),
                ('Order_Deadline', models.DateField()),
                ('keywords', models.TextField()),
                ('urls', models.TextField()),
                ('link_Type', models.CharField(max_length=300)),
                ('details', ckeditor.fields.RichTextField()),
                ('image_url', models.TextField()),
                ('terms_to_avoid', models.TextField()),
                ('info_source', models.TextField()),
                ('Status', models.CharField(choices=[('completed', 'COMPLETED'), ('to do', 'TO DO')], default='to do', max_length=20)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Order_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='randomapp.order_details')),
            ],
        ),
        migrations.CreateModel(
            name='Billing_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(max_length=300)),
                ('First_Name', models.CharField(max_length=300)),
                ('Last_Name', models.CharField(max_length=300)),
                ('Company_Name', models.CharField(max_length=300, null=True)),
                ('VAT', models.CharField(max_length=300, null=True)),
                ('Address', models.TextField()),
                ('City', models.CharField(max_length=300)),
                ('State', models.CharField(max_length=300, null=True)),
                ('Zip_Code', models.IntegerField()),
                ('Email', models.CharField(max_length=300)),
                ('Phone', models.CharField(max_length=300)),
                ('Order_Notes', models.TextField(null=True)),
                ('Order_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='randomapp.order_details')),
            ],
        ),
    ]
