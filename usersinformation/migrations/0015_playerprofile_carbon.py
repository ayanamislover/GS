# Generated by Django 5.0.2 on 2024-03-19 21:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("usersinformation", "0014_achievementanduser"),
    ]

    operations = [
        migrations.AddField(
            model_name="playerprofile",
            name="carbon",
            field=models.IntegerField(default=0),
        ),
    ]
