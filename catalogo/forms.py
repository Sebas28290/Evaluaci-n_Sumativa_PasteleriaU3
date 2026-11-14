from datetime import date
from django import forms
from .models import Encargo

class EncargoForm(forms.ModelForm):
    class Meta:
        model = Encargo
        fields = ['nombre_cliente', 'correo_cliente', 'fecha_retiro', 'cantidad_unidades']
        widgets = {
            'nombre_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre completo'}),
            'correo_cliente': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.cl'}),
            'fecha_retiro': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cantidad_unidades': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }

    def clean_fecha_retiro(self):
        fecha = self.cleaned_data['fecha_retiro']
        if fecha <= date.today():
            raise forms.ValidationError("La fecha de retiro debe ser a partir de mañana.")
        return fecha