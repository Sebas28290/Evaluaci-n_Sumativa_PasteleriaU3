from django.contrib import admin
from catalogo.models import Linea, Producto , Encargo
# Register your models here.



@admin.register (Linea)

class LineaAdmin (admin.ModelAdmin):

    list_display = ['nombre',]
    search_fields = ['nombre',]

@admin.register (Producto)

class ProductoAdmin (admin.ModelAdmin):
    list_display = ['linea', 'nombre', 'disponible', 'formato_chileno', 'stock',]
    list_filter = ['disponible', 'linea',]
    search_fields = ['nombre',]
    

    
@admin.register(Encargo)

class EncargoAdmin (admin.ModelAdmin):
    list_display = ['codigo', 'producto', 'cantidad_unidades', 'fecha_retiro',]
    list_filter = ['producto', 'fecha_retiro',]
    search_fields = ['nombre_cliente', 'correo_cliente',]
    
    
   