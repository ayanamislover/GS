# Generated by Django 4.1 on 2024-02-17 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PlayerProfile",
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
                ("nickname", models.CharField(blank=True, max_length=255)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("achievement_count", models.IntegerField(default=0)),
                ("bio", models.TextField(blank=True)),
                ("login_days", models.IntegerField(default=0)),
            ],
        ),
    ]
