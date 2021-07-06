# Generated by Django 3.1.4 on 2021-07-05 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0003_productos_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='descripcion',
            field=models.CharField(max_length=300, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='precio',
            field=models.FloatField(verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='publicado',
            field=models.BooleanField(default=True, verbose_name='¿Publicado?'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='usuario',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]