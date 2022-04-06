# Generated by Django 3.1.7 on 2022-04-06 14:26

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20220406_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='age',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='survey',
            name='country',
            field=django_countries.fields.CountryField(default=False, max_length=2),
        ),
        migrations.AddField(
            model_name='survey',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=False, max_length=20),
        ),
    ]
