# Generated by Django 4.0 on 2022-01-04 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('budget', '0004_remove_item_tags_item_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
