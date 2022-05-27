# Generated by Django 3.1.7 on 2022-05-27 14:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('horario', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Planificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('cantidadkg', models.FloatField()),
                ('estatus', models.CharField(max_length=5)),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PlE', to='industrialgip.empresa')),
                ('linea', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PlL', to='industrialgip.linea')),
                ('tp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PlTp', to='industrialgip.tp')),
            ],
        ),
        migrations.CreateModel(
            name='MateriaPrima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('empresadestino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MpE', to='industrialgip.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='DiarioProd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('hora', models.TimeField()),
                ('kilosp', models.FloatField()),
                ('desperdicios', models.IntegerField()),
                ('idrack', models.IntegerField()),
                ('observaciones', models.CharField(max_length=50)),
                ('orden', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='DpO', to='industrialgip.planificacion')),
                ('turno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DpT', to='industrialgip.turno')),
            ],
        ),
        migrations.CreateModel(
            name='DiarioMP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('ingresokg', models.FloatField()),
                ('consumokg', models.FloatField()),
                ('observaciones', models.TextField()),
                ('linea', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DmpL', to='industrialgip.linea')),
                ('materiaprima', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DmpMt', to='industrialgip.materiaprima')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DmpP', to='industrialgip.planificacion')),
                ('turno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DmpT', to='industrialgip.turno')),
            ],
        ),
    ]