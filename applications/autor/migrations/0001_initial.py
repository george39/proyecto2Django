# Generated by Django 4.0.1 on 2022-01-11 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('nacionalidad', models.CharField(max_length=30)),
                ('edad', models.PositiveIntegerField()),
                ('seudonimo', models.CharField(blank=True, max_length=50, verbose_name='seudonimo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
