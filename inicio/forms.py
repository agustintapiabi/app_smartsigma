from django import forms
from .models import Proceso, Inventario, HistoricoVenta

class AñadirProceso(forms.ModelForm):
    class Meta:
        model = Proceso
        fields = ['Name', 'Description', 'Area']

class AñadirSKU(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['SKU', 'Description', 'Area'] 

class IngresarVenta(forms.ModelForm):
    class Meta:
        model = HistoricoVenta
        fields = ['SKU', 'Cantidad', 'Precio', 'Fecha'] 