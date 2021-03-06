# Generated by Django 3.2.5 on 2021-07-04 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nombre', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=12, verbose_name='apellido')),
                ('ciudad', models.CharField(max_length=12, verbose_name='ciudad')),
                ('edad', models.CharField(blank=True, max_length=3, null=True, verbose_name='edad')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]
