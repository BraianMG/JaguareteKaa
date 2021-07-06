from paginas.models import Pagina

def get_paginas(request):
    paginas = Pagina.objects.filter(visible=True).order_by('orden').values_list('id', 'titulo', 'slug')

    return {
        'paginas': paginas,
    }