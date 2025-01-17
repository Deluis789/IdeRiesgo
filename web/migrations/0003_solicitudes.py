# Generated by Django 4.2 on 2024-07-31 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_solicitudtecnica_descripcion_trabajo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitudes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(null=True)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('en_progreso', 'En Progreso'), ('completado', 'Completado'), ('cancelado', 'Cancelado')], default='pendiente', max_length=30)),
                ('solicitud_tecnica', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.solicitudtecnica')),
                ('solicitud_vecino', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.solicitudvecino')),
            ],
        ),
    ]
