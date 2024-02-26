# Generated by Django 4.2.10 on 2024-02-25 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('location_name', models.CharField(max_length=255)),
            ],
        ),
    ]
