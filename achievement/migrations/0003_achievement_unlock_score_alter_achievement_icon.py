# Generated by Django 4.1 on 2024-02-23 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("achievement", "0002_achievement_icon_alter_achievement_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="achievement",
            name="unlock_score",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="achievement",
            name="icon",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
