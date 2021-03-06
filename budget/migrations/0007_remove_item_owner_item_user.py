# Generated by Django 4.0 on 2022-01-04 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('budget', '0006_alter_item_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='owner',
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itemOwner', to='auth.user'),
        ),
    ]
