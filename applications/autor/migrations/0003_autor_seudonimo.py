# Generated by Django 4.0.1 on 2022-01-11 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0002_remove_autor_seudonimo'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='seudonimo',
            field=models.CharField(blank=True, max_length=50, verbose_name='seudonimo'),
        ),
    ]
