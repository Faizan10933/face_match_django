# Generated by Django 4.0.1 on 2022-07-29 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_information_aadharno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='match',
            field=models.BooleanField(default=False),
        ),
    ]
