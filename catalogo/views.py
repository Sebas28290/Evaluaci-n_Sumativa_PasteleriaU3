from django.shortcuts import render
from catalogo.models import Producto, Linea
# Create your views here.
from django.shortcuts import render, get_object_or_404

def inicio_catalogo(request):
    productos = Producto.objects.filter(disponible=True)
    lineas = Linea.objects.all()

    q = request.GET.get('q', '')
    linea_id = request.GET.get('linea', '')

    if q:
        productos = productos.filter(nombre__icontains=q)
    if linea_id:
        productos = productos.filter(linea_id=linea_id)

    contexto = {
        'productos': productos,
        'lineas': lineas,
        'q': q,
        'linea_id': linea_id,
    }
    return render(request, 'catalogo/catalogo.html', contexto)

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk, disponible=True)
    return render(request, 'catalogo/detalle.html', {'producto': producto})
