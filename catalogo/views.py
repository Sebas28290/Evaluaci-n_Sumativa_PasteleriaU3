from django.shortcuts import render
from catalogo.models import Producto, Linea, Encargo
from django.shortcuts import render, get_object_or_404, redirect
from catalogo.forms import EncargoForm

# Create your views here.

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
    
    encargo_creado = None
    error_stock = None

    if request.method == 'POST':
        form = EncargoForm(request.POST)
        if form.is_valid():
            encargo = form.save(commit=False)
            if encargo.cantidad_unidades > producto.stock:
                error_stock = f"Solo quedan {producto.stock} unidades disponibles"
            else:
                encargo.producto = producto
                encargo.save()
                producto.stock -= encargo.cantidad_unidades
                producto.save()
                return redirect('comprobante_encargo', codigo=encargo.codigo)
    else:
        form = EncargoForm()

    contexto = {
        'producto': producto,
        'form': form,
        'encargo_creado': encargo_creado,
        'error_stock': error_stock,
    }

    return render(request, 'catalogo/detalle.html', contexto)


def comprobante_encargo(request, codigo):
    encargo = get_object_or_404(Encargo, codigo=codigo)
    return render(request, 'catalogo/comprobante.html', {'encargo': encargo})