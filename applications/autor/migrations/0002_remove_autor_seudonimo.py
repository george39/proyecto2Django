# Generated by Django 4.0.1 on 2022-01-11 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='seudonimo',
        ),
    ]
