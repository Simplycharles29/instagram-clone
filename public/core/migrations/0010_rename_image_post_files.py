# Generated by Django 4.2.1 on 2023-05-12 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_posts_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='files',
        ),
    ]
