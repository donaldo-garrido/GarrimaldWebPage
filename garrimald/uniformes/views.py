from django.shortcuts import render
from .forms import UniformForm
from django.forms import formset_factory
from .models import Escuela, Pedidos
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView



def home(request):
    return render(request, 'uniformes/home.html')

def administradores(request):
    return render(request, 'uniformes/administradores.html')

def ordenar(request):
    filled_form = UniformForm()
    return render(request, 'uniformes/ordenar.html', {'uniformform':filled_form})

"""def ordenar(request):
    if request.method == 'POST':
        filled_form = Pedidos(request.POST)#, request.FILES)
        if filled_form.is_valid():
            created_uniform = filled_form.save()
            created_uniform_pk = created_uniform.id

            note = ' El uniforme de %s se ha registrado' %(filled_form.cleaned_data['nombre'],)
            filled_form = Pedidos()
        else:
            created_uniform_pk = None
            note = 'Pizza order has failed. Try again.'
        return render(request, 'uniformes/ordenar.html', {'created_uniform_pk':created_uniform_pk, 'uniformform':filled_form, 'note':note})

"""