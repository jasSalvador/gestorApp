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

    def __init__(self, *args, **kwargs):
        organizacion = kwargs.pop('organizacion', None)
        super().__init__(*args, **kwargs)
        if organizacion:
            #mostrar solo integrantes de la organizacicon actual
            self.fields['integrante'].queryset = Integrante.objects.filter(organizacion=organizacion)

#gasto
class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['nombre', 'fecha']

    def __init__(self, *args, **Kwargs):
        organizacion = Kwargs.pop('organizacion', None)
        super().__init__(*args, **Kwargs)
        if organizacion:
            #forzar q el gasto se cree para la organizacion actual
            self.instance.organizacion = organizacion

#item de gasto
class ItemGastoForm(forms.ModelForm):
    class Meta:
        model = ItemGasto
        fields = ['nombre', 'monto']