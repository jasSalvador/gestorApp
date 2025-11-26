from django import forms
from .models import Integrante, Organizacion, Cuota, Gasto, ItemGasto


#organizacion
class OrganizacionForm(forms.ModelForm):
    class Meta:
        model = Organizacion
        fields = ['nombre', 'tipo']

#integrante
class IntegranteForm(forms.ModelForm):
    class Meta:
        model = Integrante
        fields = ['direccion', 'telefono', 'dependiente']

#cuota
class CuotaForm(forms.ModelForm):
    class Meta:
        model = Cuota
        fields = ['integrante','monto', 'fecha_pago', 'mes_pagado', 'anio_pagado']


#gasto
class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['organizacion', 'nombre', 'fecha']


#item de gasto
class ItemGastoForm(forms.ModelForm):
    class Meta:
        model = ItemGasto
        fields = ['nombre', 'monto']