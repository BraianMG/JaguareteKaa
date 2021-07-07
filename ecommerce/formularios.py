from django.forms import widgets
from ecommerce.models import Productos, Carritos
from django import forms
from django.core import validators

class FormProducto(forms.ModelForm):
    titulo = forms.CharField(label='Titulo',
                             widget=forms.TextInput(attrs={'type':'text', 'class':'form-control', 'placeholder':'Titulo del Producto'}),
                             max_length=100,
                             required=True,
                             help_text='Requerido. 100 caracteres o menos.')
    # imagen = forms.ImageField(label='Imagen',
    #                           required=True,
    #                           help_text='Requerido. Subir imagen, en lo posible optimizada para uso web.')
    # categoria = forms.ChoiceField(label='Categoría',
    #                               widget=forms.Select(attrs={'class':'form-select', 'aria-label':'Categoría'}),
    #                               required=True,
    #                               help_text='Requerido. Seleccione una categoria de la lista.')
    descripcion = forms.CharField(label='Descripción',
                                  widget=forms.Textarea(attrs={'type':'text', 'class':'form-control', 'placeholder':'Descripción'}),
                                  max_length=300,
                                  required=True,
                                  help_text='Requerido. Introduza una descripción para el producto.')
    precio = forms.FloatField(label='Precio: $',
                              widget=forms.NumberInput(attrs={'type':'number', 'class':'form-control w-25', 'id':'precio', 'placeholder':'XXXX.XX'}),
                              required=True,
                              help_text='Requerido. Introduza una precio para el producto.')

    class Meta:
        model = Productos
        fields = ('titulo', 'imagen', 'categoria', 'descripcion', 'precio')
        widgets = {
            'imagen': forms.FileInput(attrs={'type':'file', 'class':'form-control', 'id':'imagen'}),
            'categoria': forms.Select(attrs={'class':'form-select', 'aria-label':'Categoría'})
        }

class FormCarrito(forms.ModelForm):
    
    class Meta:
        model = Carritos
        fields = ('usuario', 'lista_productos', 'precio_total')
