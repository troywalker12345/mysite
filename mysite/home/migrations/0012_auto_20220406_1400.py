# Generated by Django 3.1.7 on 2022-04-06 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20220406_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='consider_solution',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='survey',
            name='experience',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='survey',
            name='performance_hits',
            field=models.IntegerField(default=False),
        ),
    ]
