from django.db import models
import uuid
# Create your models here.

def generar_codigo():
    return uuid.uuid4().hex[:8].upper()

class Linea (models.Model):
    nombre = models.CharField (max_length=80, unique= True)

    def __str__(self):
        return self.nombre

class Producto (models.Model):
    linea = models.ForeignKey (Linea, on_delete=models.CASCADE)
    nombre = models.CharField (max_length= 50)
    precio = models.PositiveIntegerField ()
    cantidad_porciones = models.PositiveIntegerField ()
    apto_celiaco = models.BooleanField ()
    stock = models.IntegerField()
    imagen = models.ImageField (upload_to='productos/', blank=True, null=True)
    disponible = models.BooleanField(default=True)

    def preciototal (self):
        return self.precio * self.cantidad_porciones
    
    def __str__(self):
        return f"{self.linea.nombre} - {self.nombre}"

class Encargo (models.Model):
    producto = models.ForeignKey (Producto, on_delete=models.CASCADE)
    nombre_cliente = models.CharField (max_length=80)
    correo_cliente = models.EmailField ()
    fecha_retiro = models.DateField ()
    cantidad_unidades = models.PositiveIntegerField ()
    fecha_hora_encargo = models.DateTimeField (auto_now_add=True)
    codigo = models.CharField (max_length=8, unique=True, default=generar_codigo, editable= False)

    
    def cantidadtotal (self):
        return self.cantidad_unidades * self.producto.precio
    
    def __str__(self):
        return f"{self.nombre_cliente} - {self.fecha_retiro}"

    