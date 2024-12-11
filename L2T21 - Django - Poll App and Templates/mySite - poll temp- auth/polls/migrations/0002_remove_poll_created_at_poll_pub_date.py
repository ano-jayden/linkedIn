# Generated by Django 5.1.1 on 2024-09-25 14:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='created_at',
        ),
        migrations.AddField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)),
        ),
    ]
