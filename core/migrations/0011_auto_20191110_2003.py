# Generated by Django 2.2.6 on 2019-11-10 23:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20191109_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='published_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
