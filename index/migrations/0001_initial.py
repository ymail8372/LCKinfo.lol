# Generated by Django 5.0.1 on 2024-05-28 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Champion_LCK_2023_summer',
            fields=[
                ('key', models.AutoField(db_column='key', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='name', default='-')),
                ('pick', models.IntegerField(db_column='pick', default=0)),
                ('ban', models.IntegerField(db_column='ban', default=0)),
                ('win', models.IntegerField(db_column='win', default=0)),
                ('lose', models.IntegerField(db_column='lose', default=0)),
                ('patch', models.TextField(db_column='patch', default='-')),
            ],
            options={
                'db_table': 'champion_LCK_2023_summer',
            },
        ),
        migrations.CreateModel(
            name='Champion_LCK_2024_spring',
            fields=[
                ('key', models.AutoField(db_column='key', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='name', default='-')),
                ('pick', models.IntegerField(db_column='pick', default=0)),
                ('ban', models.IntegerField(db_column='ban', default=0)),
                ('win', models.IntegerField(db_column='win', default=0)),
                ('lose', models.IntegerField(db_column='lose', default=0)),
                ('patch', models.TextField(db_column='patch', default='-')),
            ],
            options={
                'db_table': 'champion_LCK_2024_spring',
            },
        ),
        migrations.CreateModel(
            name='Champion_MSI_2024',
            fields=[
                ('key', models.AutoField(db_column='key', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='name', default='-')),
                ('pick', models.IntegerField(db_column='pick', default=0)),
                ('ban', models.IntegerField(db_column='ban', default=0)),
                ('win', models.IntegerField(db_column='win', default=0)),
                ('lose', models.IntegerField(db_column='lose', default=0)),
                ('patch', models.TextField(db_column='patch', default='-')),
            ],
            options={
                'db_table': 'champion_MSI_2024',
            },
        ),
        migrations.CreateModel(
            name='Ranking_LCK_2023_spring',
            fields=[
                ('key', models.AutoField(db_column='key', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='name', default='-')),
                ('tricode', models.TextField(db_column='tricode', default='-')),
                ('match_win', models.IntegerField(db_column='match_win', default=0)),
                ('match_lose', models.IntegerField(db_column='match_lose', default=0)),
                ('set_win', models.IntegerField(db_column='set_win', default=0)),
                ('set_lose', models.IntegerField(db_column='set_lose', default=0)),
                ('etc', models.TextField(db_column='etc', default='-')),
            ],
            options={
                'db_table': 'ranking_LCK_2023_spring',
            },
        ),
        migrations.CreateModel(
            name='Ranking_LCK_2023_summer',
            fields=[
                ('key', models.AutoField(db_column='key', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='name', default='-')),
                ('tricode', models.TextField(db_column='tricode', default='-')),
                ('match_win', models.IntegerField(db_column='match_win', default=0)),
                ('match_lose', models.IntegerField(db_column='match_lose', default=0)),
                ('set_win', models.IntegerField(db_column='set_win', default=0)),
                ('set_lose', models.IntegerField(db_column='set_lose', default=0)),
                ('etc', models.TextField(db_column='etc', default='-')),
            ],
            options={
                'db_table': 'ranking_LCK_2023_summer',
            },
        ),
        migrations.CreateModel(
            name='Ranking_LCK_2024_spring',
            fields=[
                ('key', models.AutoField(db_column='key', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='name', default='-')),
                ('tricode', models.TextField(db_column='tricode', default='-')),
                ('match_win', models.IntegerField(db_column='match_win', default=0)),
                ('match_lose', models.IntegerField(db_column='match_lose', default=0)),
                ('set_win', models.IntegerField(db_column='set_win', default=0)),
                ('set_lose', models.IntegerField(db_column='set_lose', default=0)),
                ('etc', models.TextField(db_column='etc', default='-')),
            ],
            options={
                'db_table': 'ranking_LCK_2024_spring',
            },
        ),
        migrations.CreateModel(
            name='Ranking_LCK_2024_spring_player',
            fields=[
                ('key', models.AutoField(db_column='key', primary_key=True, serialize=False)),
                ('nickname', models.TextField(db_column='nickname', default='-')),
                ('name', models.TextField(db_column='name', default='-')),
                ('team', models.TextField(db_column='team', default='-')),
                ('tricode', models.TextField(db_column='tricode', default='-')),
                ('position', models.TextField(db_column='position', default='-')),
                ('POG_point', models.IntegerField(db_column='POG_point', default=0)),
            ],
            options={
                'db_table': 'ranking_LCK_2024_spring_player',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('key', models.AutoField(db_column='key', primary_key=True, serialize=False)),
                ('team1_name', models.TextField(db_column='team1_name', default='-')),
                ('team2_name', models.TextField(db_column='team2_name', default='-')),
                ('team1_tricode', models.TextField(db_column='team1_tricode', default='-')),
                ('team2_tricode', models.TextField(db_column='team2_tricode', default='-')),
                ('team1_score', models.IntegerField(db_column='team1_score', default=0)),
                ('team2_score', models.IntegerField(db_column='team2_score', default=0)),
                ('date', models.DateTimeField(db_column='date', default=datetime.datetime(2000, 1, 1, 0, 0))),
                ('tournament', models.TextField(db_column='tournament', default='-')),
                ('etc', models.TextField(db_column='etc')),
            ],
            options={
                'db_table': 'schedule',
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('key', models.AutoField(db_column='key', primary_key=True, serialize=False)),
                ('league_version', models.TextField(db_column='league_version', default='-')),
                ('live_version', models.TextField(db_column='live_version', default='-')),
            ],
            options={
                'db_table': 'version',
            },
        ),
    ]
