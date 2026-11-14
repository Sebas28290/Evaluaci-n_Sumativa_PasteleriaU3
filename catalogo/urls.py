from django.contrib import admin
from django.urls import path
from catalogo import views

urlpatterns = [
    path ('', views.inicio_catalogo, name='catalogo'),
]
