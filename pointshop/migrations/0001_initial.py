# Generated by Django 5.0.2 on 2024-02-29 05:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="product_images/")),
                ("price", models.IntegerField()),
                ("description", models.TextField()),
                ("sales", models.IntegerField(default=0)),
            ],
        ),
    ]
