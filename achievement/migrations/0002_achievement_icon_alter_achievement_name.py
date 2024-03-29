# Generated by Django 4.1 on 2024-02-23 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("achievement", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="achievement",
            name="icon",
            field=models.ImageField(blank=True, null=True, upload_to="achievements/"),
        ),
        migrations.AlterField(
            model_name="achievement",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]