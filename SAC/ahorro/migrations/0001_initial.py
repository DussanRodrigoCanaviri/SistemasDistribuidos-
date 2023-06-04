# Generated by Django 4.0 on 2023-05-23 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracion', '0004_persona_fecha_nacimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ahorro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debito', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('credito', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('saldo', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('fecha', models.DateTimeField(verbose_name='Fecha de operacion')),
                ('cajera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.cajera')),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.socio')),
            ],
        ),
    ]