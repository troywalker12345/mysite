# Generated by Django 4.0.3 on 2022-04-13 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_survey_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
