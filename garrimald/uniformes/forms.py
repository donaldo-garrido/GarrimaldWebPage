from django import forms
from .models import Pedidos

class HombreForm(forms.ModelForm):

    class Meta:
        model = Pedidos
        fields = ['escuela', 'nombre', 'chamarra', 'chamarra_largo','chamarra_cantidad', 
                  'playera', 'playera_largo', 'playera_cantidad',
                  'pants', 'pants_largo', 'pants_cantidad',
                  'sueter_hombre', 'sueter_hombre_largo', 'sueter_hombre_cantidad',
                  'camisa', 'camisa_cantidad',
                  'pantalon', 'pantalon_cantidad',
                  'bordados', 'bordado_nombre', 'celular']

class MujerForm(forms.ModelForm):

    class Meta:
        model = Pedidos
        fields = ['escuela', 'nombre', 'chamarra', 'chamarra_largo','chamarra_cantidad', 
                  'playera', 'playera_largo', 'playera_cantidad',
                  'pants', 'pants_largo', 'pants_cantidad',
                  'sueter_mujer', 'sueter_mujer_largo', 'sueter_mujer_cantidad',
                  'blusa', 'blusa_cantidad',
                  'jumper', 'jumper_cantidad',
                  'bordados', 'bordado_nombre', 'celular']