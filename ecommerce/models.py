from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Categorias(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.CharField(max_length=250, verbose_name="Descripción")
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    actualizado_el = models.DateTimeField(auto_now=True, verbose_name="Editado")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
    
    def __str__(self):
        return f"{self.nombre}"

class Productos(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    # descripcion = RichTextField(verbose_name="Descripción")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(default='null', verbose_name="Imagen", upload_to="productos")
    precio = models.FloatField(verbose_name="Precio")
    publicado = models.BooleanField(verbose_name="¿Publicado?", default=True)
    usuario = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    # usuario = models.ForeignKey(User, editable=False, verbose_name="Usuario", on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, verbose_name="Categorias", on_delete=models.CASCADE, blank=True)
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    actualizado_el = models.DateTimeField(auto_now=True, verbose_name="Editado")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-creado_el']

    def __str__(self):
        return f"{self.titulo}"

class Carritos(models.Model):
    usuario = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    lista_productos = models.ManyToManyField(Productos, verbose_name="Carrito")
    precio_total = models.FloatField()
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    actualizado_el = models.DateTimeField(auto_now=True, verbose_name="Editado")

    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"
        ordering = ['-creado_el']
        
    def __str__(self):
        return f"Carrito de {self.usuario} del {self.actualizado_el}"