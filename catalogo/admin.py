from django.contrib import admin
from catalogo.models import Linea, Producto , Encargo
# Register your models here.


@admin.register(Linea)

class LineaAdmin (admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',) 


@admin.register(Producto)

class ProductoAdmin(admin.ModelAdmin):

	list_display = ['linea', 'disponible', 'stock' 'formato_chileno', ]
    list_filter = ['linea', 'apto_celiaco',]

    def formato_chileno(self, obj):
        return f'${obj.precio:,}'.replace (',','.')
