from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from ecommerce.models import Categorias, Productos
from django.db.models import Q
from .formularios import FormProducto, FormCarrito
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if "carrito" not in request.session:
        request.session["carrito"] = []

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
        "carrito": request.session["carrito"],
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
                messages.success(request, 'Producto editado correctamente!')
                return redirect('inicio')
            else:
                messages.success(request, 'Error al crear el producto!')
                return redirect('nuevo-pruducto')
        else:
            form_producto = FormProducto(instance = el_producto)
            return render(request, 'productos/editar_producto.html',{
                'titulo_pagina': 'Editando Producto',
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


def agregar_al_carrito(request, id_producto):
    el_producto = get_object_or_404(Productos, id=id_producto)
    for id in request.session["carrito"]:
        if id == id_producto:
            #existe el articulo
            messages.warning(request, 'El producto ya se encuentra en su carrito')
            return HttpResponseRedirect(reverse("detalle_producto", args=(el_producto.id,)))            
    request.session["carrito"] += [id_producto]
    # request.session["carrito"] += ({'id_producto': id_producto,
    #                                    'descripcion': el_producto.descripcion,
    #                                    'precio':el_producto.precio})
    messages.success(request, 'Producto agregado correctamente!')
    return HttpResponseRedirect(reverse("detalle_producto", args=(el_producto.id,)))


def carrito(request):
    if not request.user.is_authenticated:
        return redirect('inicio')

    if request.user.is_staff:
        return redirect('inicio')

    productos = Productos.objects.filter(id__in=request.session["carrito"]).values_list('id', 'descripcion', 'precio')
    total = 0
    for producto in productos:
        total += producto[2]
    return render(request, 'productos/carrito.html',{
                'titulo_pagina': 'Carrito',
                'carrito': productos,
                'total': total,
            })

def eliminar_prod_carrito(request, id_producto):
    if not request.user.is_authenticated:
        return redirect('inicio')

    if request.user.is_staff:
        return redirect('inicio')

    if id_producto == 0:
        productos = []
        request.session["carrito"] = []
    else:
        # Significa que elimina solo un producto del carrito
        ids = request.session["carrito"]
        request.session["carrito"] = []
        for id in ids:
            if id != id_producto:
                request.session["carrito"] += [id]
    
    productos = Productos.objects.filter(id__in=request.session["carrito"]).values_list('id', 'descripcion', 'precio')
    total = 0
    for producto in productos:
        total += producto[2]
    return render(request, 'productos/carrito.html',{
                'titulo_pagina': 'Carrito',
                'carrito': productos,
                'total': total,
            })