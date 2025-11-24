from django import forms
from .models import Integrante, Organizacion


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

#