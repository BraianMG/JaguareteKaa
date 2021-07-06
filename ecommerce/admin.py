from django.contrib import admin
from .models import Categorias, Productos

class CategoriasAdmin(admin.ModelAdmin):
    readonly_fields = ('creado_el', 'actualizado_el')
    search_fields = ('nombre', 'descripcion')
    list_display = ('nombre', 'creado_el')
    ordering = ('-creado_el',)

class ProductosAdmin(admin.ModelAdmin):
    readonly_fields = ('usuario', 'creado_el', 'actualizado_el') 
    search_fields = ('titulo', 'descripcion')
    list_filter = ('publicado', 'usuario__username', 'categoria__nombre')
    list_display = ('titulo', 'precio', 'usuario', 'publicado', 'creado_el')
    ordering = ('-creado_el',) 

    def save_model(self, request, obj, form, change):
        if not obj.usuario_id:
            obj.usuario_id = request.user.id
        obj.save()

# Register your models here.
admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(Productos, ProductosAdmin)
