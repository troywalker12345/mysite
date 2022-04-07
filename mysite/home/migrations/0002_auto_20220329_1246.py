# Generated by Django 3.1.7 on 2022-03-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='question',
        ),
        migrations.AddField(
            model_name='survey',
            name='consider_valid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='survey',
            name='crypto_as_monetization',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='survey',
            name='heard_of_cryptocurrency',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='survey',
            name='purchased_cryptocurrency',
            field=models.BooleanField(default=False),
        ),
    ]