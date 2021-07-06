from django.contrib import admin
from .models import Pagina

# Configuración extra
class PaginasAdmin(admin.ModelAdmin):
    readonly_fields = ('creado_el', 'modificado_el')
    search_fields = ('titulo',)
    list_filter = ('visible',)
    list_display = ('titulo', 'visible', 'creado_el')
    ordering = ('-creado_el',)

# Register your models here.
admin.site.register(Pagina, PaginasAdmin)

# Configuración del Panel
titulo = "JAGUARETE KAA"
subtitulo = "Panel de Gestión"

admin.site.site_header = titulo
admin.site.site_title = titulo
admin.site.index_title = subtitulo