# Generated by Django 4.2.1 on 2023-05-17 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_likepost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]