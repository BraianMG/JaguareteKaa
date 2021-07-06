from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from ecommerce.models import Categorias, Productos
from django.db.models import Q
from .formularios import FormProducto
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    ultimos_productos = Productos.objects.filter(publicado=True).order_by('-id')[:3]
    demas_productos = Productos.objects.filter(publicado=True).order_by('-id')[3:10]

    # try:
    #     articulo = Productos.objects.get(title="Superman", public=False)
    #     response = f"Articulo:<br>{articulo.id}. {articulo.title}"
    # except:
    #     response = "<h1>Artículo no encontrado</h1>"

    # El 3er parametro que va entre {} son las variables que le envio a las Templates
    return render(request, 'productos/index.html',{
        'titulo_pagina': 'Inicio',
        'productos': ultimos_productos,
        'demas_productos': demas_productos,
    })

def busqueda(request, id_categoria=-1, palabra=''):

    if id_categoria != -1:
        # busqueda = Categorias.objects.values_list('nombre').get(id=id_categoria)
        busqueda = get_list_or_404(Categorias, id=id_categoria)
        # productos = Productos.objects.filter(publicado=True, categoria=id_categoria)
        productos = get_list_or_404(Productos, publicado=True, categoria=id_categoria)
    elif palabra != '':
        busqueda = palabra
        productos = Productos.objects.filter(
                                                Q(titulo__contains="algo") | Q(descripcion__contains="algo")
                                            )

    # try:
    #     articulo = Article.objects.get(title="Superman", public=False)
    #     response = f"Articulo:<br>{articulo.id}. {articulo.title}"
    # except:
    #     response = "<h1>Artículo no encontrado</h1>"

    return render(request, 'productos/busqueda.html',{
        'titulo_pagina': 'Búsqueda',
        'busqueda': busqueda,
        'productos': productos,
    })

def detalle_producto(request, id_producto):
    producto = get_list_or_404(Productos, id=id_producto, publicado=True)

    return render(request, 'productos/detalle_producto.html', {
        'titulo_pagina': 'Detalle de Producto',
        'producto': producto,
    })

def nuevo_producto(request):
    if not request.user.is_authenticated:
        return redirect('inicio')
    else:
        form_producto = FormProducto()

        if request.method == 'POST':
            user = User.objects.get(username=request.user)
            # Con este if evito errores cuando no cargan una imagen
            if request.FILES:
                form_producto = FormProducto(request.POST, request.FILES, instance=Productos(imagen=request.FILES['imagen'], usuario=user))
            else:
                form_producto = FormProducto(request.POST, request.FILES, instance=Productos(usuario=user))

            if form_producto.is_valid():
                form_producto.save()
                messages.success(request, 'Producto creado correctamente!')
                return redirect('inicio')
            else:
                messages.success(request, 'Error al crear el producto!')
                return redirect('nuevo-pruducto')

        return render(request, 'productos/nuevo_producto.html',{
            'titulo_pagina': 'Creando Producto',
            'form_producto': form_producto,
        })

def editar_producto(request, id_producto):
    if not request.user.is_authenticated:
        return redirect('inicio')
    else:
        # form_producto = FormProducto()
        el_producto = get_object_or_404(Productos, id=id_producto)
        if request.method == 'POST':
            user = User.objects.get(username=request.user)
            el_producto.usuario = user
            form_producto = FormProducto(data=request.POST, files=request.FILES, instance=el_producto)
            if form_producto.is_valid():
                form_producto.save()
                messages.success(request, 'Producto creado correctamente!')
                return redirect('inicio')
            else:
                messages.success(request, 'Error al crear el producto!')
                return redirect('nuevo-pruducto')
        else:
            form_producto = FormProducto(instance = el_producto)
            return render(request, 'productos/editar_producto.html',{
                'titulo_pagina': 'Creando Producto',
                'el_producto': el_producto,
                'form_producto': form_producto,
            })

def eliminar_producto(request, id_producto):
    if not request.user.is_authenticated:
        return redirect('inicio')
    else:
        el_producto = get_object_or_404(Productos, id=id_producto)
        el_producto.delete()
        messages.success(request, 'Producto eliminado correctamente!')
        return redirect("inicio")