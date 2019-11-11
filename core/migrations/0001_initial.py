# Generated by Django 2.2.6 on 2019-11-08 02:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='Casas')),
                ('direccion', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=3, max_digits=19)),
                ('cant_habitaciones', models.IntegerField()),
                ('cant_baños', models.IntegerField()),
                ('metros_2', models.DecimalField(decimal_places=3, max_digits=19)),
                ('patio', models.BooleanField()),
                ('tipo_contacto', models.CharField(choices=[('V', 'Venta'), ('C', 'Compra')], max_length=1)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
            ],
            options={
                'verbose_name': 'Casa',
                'verbose_name_plural': 'Casas',
                'ordering': ['-created_date'],
            },
        ),
    ]
