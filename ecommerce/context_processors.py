from ecommerce.models import Categorias, Productos

def get_ecommerce(request):

    ids_categorias_usadas = Productos.objects.filter(publicado=True).values_list('categoria', flat=True)
    categorias = Categorias.objects.filter(id__in=ids_categorias_usadas).values_list('id', 'nombre')

    return {
        'categorias': categorias,
    }