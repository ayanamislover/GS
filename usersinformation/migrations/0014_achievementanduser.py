# Generated by Django 4.2.11 on 2024-03-19 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("achievement", "0006_alter_achievement_icon"),
        ("usersinformation", "0013_remove_playerprofile_user_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AchievementAndUser",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "achievement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="achievement.achievement",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usersinformation.playerprofile",
                    ),
                ),
            ],
        ),
    ]
