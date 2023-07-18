from django import forms
from .models import Pedidos

class UniformForm(forms.ModelForm):

    class Meta:
        model = Pedidos
        fields = ['escuela', 'nombre', 'chamarra', 'chamarra_cantidad', 'bordado_nombre', 'celular']
        labels = {
            'escuela':'Escuela', 'nombre':'Nombre', 'chamarra':'Talla chamarra', 
            'chamarra_cantidad':'Cantidad', 'bordado_nombre':'Nombre en el bordado', 'celular':'Celular'
        }