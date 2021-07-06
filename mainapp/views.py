from django.shortcuts import render, redirect
from django.contrib import messages
from .formularios import FormRegistro
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def acerca_de(request):
    return render(request, 'mainapp/acerca_de.html',{
        'titulo_pagina': 'Acerca de',
    })

def contacto(request):
    return render(request, 'mainapp/contacto.html',{
        'titulo_pagina': 'Contacto',
    })

def pagina_registro(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        form_registro = FormRegistro()

        if request.method == 'POST':
            form_registro = FormRegistro(request.POST)
            if form_registro.is_valid():
                form_registro.save()
                messages.success(request, 'Te has registrado correctamente!')
                return redirect('inicio')

        return render(request, 'usuarios/registro.html', {
            'titulo_pagina': 'Registrate en nuestra Web',
            'form_registro': form_registro,
        })

def pagina_login(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method == 'POST':
            usuario = request.POST.get('usuario')
            contrasenia = request.POST.get('contrasenia')

            user = authenticate(request, username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido/a {request.user.username}')
                return redirect('inicio')
            else:
                messages.warning(request, 'No te has identificado correctamente')

        return render(request, 'usuarios/login.html',{
            'titulo_pagina': 'Acceder a la Web',
            # 'form_registro': form_registro,
        })

def cerrar_sesion(request):
    logout(request)
    return redirect('pagina_login')