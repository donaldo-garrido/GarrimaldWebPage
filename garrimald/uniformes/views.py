# Importamos las librerías necesarias
from django.shortcuts import render
from django.forms import formset_factory
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

# Importamos funciones y clases
from .forms import HombreForm
from .models import Escuela, Pedidos

# -----------------------------------------------
# Función para el Inicio
def home(request):
    return render(request, 'uniformes/home.html')

# -----------------------------------------------
# Función para iniciar sesión
class LoginInterfaceView(LoginView):
    template_name = 'uniformes/login.html'


# -----------------------------------------------
# Función para cerrar sesión
class LogoutInterfaceView(LogoutView):
    template_name = 'uniformes/logout.html'


# -----------------------------------------------
# Función para ir a la página de administradores
@login_required(login_url='login')
def administradores(request):
    return render(request, 'uniformes/administradores.html')


# -----------------------------------------------
# Función para ordenar un pedido
@login_required(login_url='login')
def ordenar(request):
    filled_form = HombreForm()
    if request.method == 'POST':
        filled_form = HombreForm(request.POST)
        if filled_form.is_valid():
            created_uniform = filled_form.save()
            created_uniform_pk = created_uniform.id

            print(created_uniform_pk)

        return render(request, 'uniformes/ordenar.html', {'uniformform':filled_form})
    else: return render(request, 'uniformes/ordenar.html', {'uniformform':filled_form})

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

# -----------------------------------------------
# Función para ver un pedido (externo)
def ver(request):
    return render(request, 'uniformes/ver.html')

# -----------------------------------------------
# Función para editar un pedido
@login_required(login_url='login')
def editar(request):
    return render(request, 'uniformes/editar.html')

# -----------------------------------------------
# Función para 
@login_required(login_url='login')
def capital(request):
    return render(request, 'uniformes/capital.html')


# -----------------------------------------------
# Función para 
@login_required(login_url='login')
def dbase(request):
    return render(request, 'uniformes/dbase.html')

