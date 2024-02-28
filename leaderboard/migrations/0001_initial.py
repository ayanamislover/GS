# Generated by Django 5.0.2 on 2024-02-23 00:23

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="leaderboard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=150)),
                ("score", models.IntegerField(default=0)),
                ("achievements", models.IntegerField(default=0)),
                ("login_days", models.IntegerField(default=0)),
                ("carbon_footprint", models.FloatField(default=0.0)),
            ],
        ),
    ]