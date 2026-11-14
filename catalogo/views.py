from django.shortcuts import render
from catalogo.models import Producto
# Create your views here.


def inicio_catalogo(request):
    productos = Producto.objects.filter(disponible=True)
    return render(request, 'catalogo/catalogo.html', {'productos': productos})