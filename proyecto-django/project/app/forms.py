from django import forms
from .models import Persona, Barrio, LocalComida, LocalRepuesto

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombres', 'apellidos', 'cedula', 'correo']

class BarrioForm(forms.ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre', 'siglas']

class LocalComidaForm(forms.ModelForm):
    class Meta:
        model = LocalComida
        fields = ['propietario', 'direccion', 'barrio', 'tipo_comida', 'ventas_proyectadas']

class LocalRepuestoForm(forms.ModelForm):
    class Meta:
        model = LocalRepuesto
        fields = ['propietario', 'direccion', 'barrio', 'valor_mercaderia']
