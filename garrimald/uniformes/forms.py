from django import forms
from .models import Pedidos

class HombreForm(forms.ModelForm):

    class Meta:
        model = Pedidos
        fields = ['escuela', 'nombre', 'chamarra', 'chamarra_largo','chamarra_cantidad', 
                  'playera', 'playera_largo', 'playera_cantidad',
                  'pants', 'pants_largo', 'pants_cantidad',
                  'sueter', 'sueter_largo', 'sueter_cantidad',
                  'camisa', 'camisa_cantidad',
                  'pantalon', 'pantalon_cantidad',
                  'bordados', 'bordado_nombre', 'celular']