# Generated by Django 4.0 on 2022-01-20 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0008_alter_item_user'),
        ('user', '0005_sheet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sheet',
            name='items',
        ),
        migrations.AddField(
            model_name='sheet',
            name='items',
            field=models.ManyToManyField(null=True, to='budget.Item'),
        ),
    ]
