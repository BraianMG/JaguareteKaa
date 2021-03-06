# Generated by Django 3.1.4 on 2021-07-02 22:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=250, verbose_name='Descripción')),
                ('creado_el', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('descripcion', ckeditor.fields.RichTextField(verbose_name='Descripción')),
                ('imagen', models.ImageField(default='null', upload_to='productos', verbose_name='Imagen')),
                ('precio', models.FloatField(verbose_name='Título')),
                ('publicado', models.BooleanField(verbose_name='¿Publicado?')),
                ('creado_el', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('actualizado_el', models.DateTimeField(auto_now=True, verbose_name='Editado')),
                ('categoria', models.ManyToManyField(blank=True, null=True, to='ecommerce.Categorias', verbose_name='Categorias')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['-creado_el'],
            },
        ),
    ]
