# Importamos las librerías necesarias
from django.shortcuts import render
from django.forms import formset_factory
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

# Importamos funciones y clases
from .forms import HombreForm, MujerForm
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
# Función para hacer filtrado de sexo del niñ@
@login_required(login_url='login')
def sexo(request):
    return render(request, 'uniformes/sexo.html')

# -----------------------------------------------
# Función para ordenar un pedido de niño
@login_required(login_url='login')
def ordenarMujer(request):
    filled_form = MujerForm()
    if request.method == 'POST':
        filled_form = MujerForm(request.POST)
        if filled_form.is_valid():
            created_uniform = filled_form.save()
            created_uniform_pk = created_uniform.id

            print(created_uniform_pk)
            print(created_uniform.nombre)
            print(created_uniform.sueter_mujer_largo)
            #note = 'El uniforme de %s fue ordenado\nEscuela: %s \n%s Sueter T-%s \n%s Jumper T-%s \n%s Blusa T-%s \n%s Chamarra T-%s \n%s Pants T-%s \n%s Playera T-%s \nCon %sBordados' 

        return render(request, 'uniformes/ordenarMujer.html', {'uniformform':filled_form})
    else: return render(request, 'uniformes/ordenarMujer.html', {'uniformform':filled_form})


# -----------------------------------------------
# Función para ordenar un pedido de niño
@login_required(login_url='login')
def ordenarHombre(request):
    filled_form = HombreForm()
    if request.method == 'POST':
        filled_form = HombreForm(request.POST)
        if filled_form.is_valid():
            created_uniform = filled_form.save()
            created_uniform_pk = created_uniform.id

            print(created_uniform_pk)

        return render(request, 'uniformes/ordenarHombre.html', {'uniformform':filled_form})
    else: return render(request, 'uniformes/ordenarHombre.html', {'uniformform':filled_form})

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

