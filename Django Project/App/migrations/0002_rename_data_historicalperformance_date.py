# Generated by Django 4.2.7 on 2023-11-23 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalperformance',
            old_name='data',
            new_name='date',
        ),
    ]
