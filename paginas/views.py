from django.shortcuts import render
from .models import Pagina

# Create your views here.
def pagina(request, slug):
    pagina = Pagina.objects.get(slug=slug)

    return render(request, "paginas/pagina.html", {
        "pagina": pagina,
    })