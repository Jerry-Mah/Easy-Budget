# Generated by Django 4.0 on 2022-01-20 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0008_alter_item_user'),
        ('user', '0006_remove_sheet_items_sheet_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='items',
            field=models.ManyToManyField(to='budget.Item'),
        ),
    ]