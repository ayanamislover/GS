# Generated by Django 4.2.10 on 2024-03-14 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navi', '0004_checker_overview_checker_picture_checker_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checker',
            name='picture',
            field=models.TextField(default='navi/static/images/Journey-amico.png'),
        ),
    ]
