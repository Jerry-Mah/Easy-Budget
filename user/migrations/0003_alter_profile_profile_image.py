# Generated by Django 4.0 on 2022-01-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='user-default.png', null=True, upload_to=''),
        ),
    ]
