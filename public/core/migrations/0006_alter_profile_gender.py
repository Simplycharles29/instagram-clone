# Generated by Django 4.2.1 on 2023-05-11 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.IntegerField(choices=[('male', 'male'), ('female', 'female'), ('none', 'none')], default='none'),
        ),
    ]
