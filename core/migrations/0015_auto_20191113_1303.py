# Generated by Django 2.2.6 on 2019-11-13 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_galeria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galeria',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='galeria',
            name='titulo',
        ),
    ]
