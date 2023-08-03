from django import forms
from .models import Pedidos, Total

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
        

class CuentaForm(forms.ModelForm):

    class Meta:
        model = Total
        fields = ['a_cuenta', 'entregado']



class VerForm(forms.Form):
    ver_pk = forms.IntegerField(label='No. de pedido')
    celular = forms.IntegerField(label='Celular')


class SexoForm(forms.Form):
    sexo = forms.ChoiceField(label='Sexo', choices=[(0,'Mujer'),(1,'Hombre')])