# Generated by Django 5.1.dev20240127105402 on 2024-02-27 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]