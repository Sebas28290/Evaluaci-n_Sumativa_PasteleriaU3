from django.contrib import admin
from django.urls import path
from catalogo import views

urlpatterns = [
    path ('', views.inicio_catalogo, name='catalogo'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path ('comprobante/<str:codigo>/', views.comprobante_encargo, name='comprobante_encargo')
]
