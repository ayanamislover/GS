# Generated by Django 4.1 on 2024-02-24 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("answerquestion", "0003_remove_question_pub_date_question_series_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="question", name="score", field=models.IntegerField(default=1),
        ),
    ]