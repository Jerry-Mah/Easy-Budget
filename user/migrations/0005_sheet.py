# Generated by Django 4.0 on 2022-01-20 08:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('budget', '0008_alter_item_user'),
        ('user', '0004_alter_profile_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('items', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.item')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
