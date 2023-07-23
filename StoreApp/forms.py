from django import forms
from .models import Productos, Clientes, Ventas

#Formulario Productos
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'

#Formulario clientes
class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'

#Formulario ventas
class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = '__all__'
