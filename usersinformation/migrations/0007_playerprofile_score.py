# Generated by Django 4.1 on 2024-02-23 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usersinformation", "0006_alter_playerprofile_achievements"),
    ]

    operations = [
        migrations.AddField(
            model_name="playerprofile",
            name="score",
            field=models.IntegerField(default=0),
        ),
    ]
