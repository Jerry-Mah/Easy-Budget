# Generated by Django 4.0 on 2022-02-16 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_itemclone'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemclone',
            name='id_filter',
            field=models.CharField(max_length=100, null=True),
        ),
    ]