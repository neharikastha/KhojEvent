# Generated by Django 5.0 on 2024-03-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_address_organiser_area_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organiser',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
