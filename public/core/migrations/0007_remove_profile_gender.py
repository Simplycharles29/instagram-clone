# Generated by Django 4.2.1 on 2023-05-11 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_profile_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
    ]
