# Generated by Django 5.0.2 on 2024-02-27 18:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("activityboard", "0006_alter_quizsession_unique_together"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Player",
        ),
        migrations.RemoveField(
            model_name="quizsession",
            name="timestamp",
        ),
    ]