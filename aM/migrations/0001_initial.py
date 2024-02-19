# Generated by Django 5.1.dev20240127105402 on 2024-02-18 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('max_participants', models.PositiveIntegerField()),
                ('fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('draft', 'Draft 草稿'), ('published', 'Published 发布'), ('ended', 'Ended 结束')], default='draft', max_length=20)),
                ('organizer', models.CharField(max_length=120)),
                ('category', models.CharField(max_length=50)),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
