# Generated by Django 4.0 on 2022-01-20 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_sheet_items'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sheet',
        ),
    ]
