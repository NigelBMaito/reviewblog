# Generated by Django 5.1.4 on 2024-12-30 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='banners/'),
        ),
    ]
