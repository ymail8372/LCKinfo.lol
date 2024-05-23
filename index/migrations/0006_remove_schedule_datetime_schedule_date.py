# Generated by Django 4.0.3 on 2024-05-23 20:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_champion_2024_msi_delete_ranking_2024_msi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='datetime',
        ),
        migrations.AddField(
            model_name='schedule',
            name='date',
            field=models.DateTimeField(db_column='date', default=datetime.datetime(2000, 1, 1, 0, 0)),
        ),
    ]
