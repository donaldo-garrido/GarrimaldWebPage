# Importamos las librerías necesarias
from django.shortcuts import render
from django.forms import formset_factory
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
import pandas as pd

# Importamos funciones y clases
from .forms import HombreForm, MujerForm
from .models import Precios

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
# Función para calcular total
@login_required(login_url='login')
def calcularTotal():
    formset = MujerForm()



# -----------------------------------------------
# Función para ordenar un pedido de niño
@login_required(login_url='login')
def ordenarMujer(request):
    formset = MujerForm()
    if request.method == 'POST':
        filled_form = MujerForm(request.POST)
        
        if filled_form.is_valid():
            created_uni = filled_form.save()
            created_uniform_pk = created_uni.id

            precios = Precios.objects.get(pk=created_uni.escuela_id)
            print(precios)
            print(precios.pantalon_cantidad)
            print('........................................')

            list_finalizar = []

            if created_uni.playera_cantidad != 0:
                prenda = 'Playera'
                cantidad = created_uni.playera_cantidad
                precio = precios.playera_cantidad
                total = cantidad*precio
                dict_finalizar = {'prenda':prenda,'cantidad':cantidad,
                                  'precio':precio, 'total':total}
                
                list_finalizar.append(dict_finalizar)


            #if created_uniform.
            

            print(created_uniform_pk)
            print(created_uni.nombre)
            print(created_uni.sueter_mujer_largo)
            #note = 'El uniforme de %s fue ordenado\nEscuela: %s \n%s Sueter T-%s \n%s Jumper T-%s \n%s Blusa T-%s \n%s Chamarra T-%s \n%s Pants T-%s \n%s Playera T-%s \nCon %sBordados' 

        return render(request, 'uniformes/finalizar.html', {'created_uniform_pk':created_uniform_pk, 'dict_finalizar':list_finalizar})
    else: return render(request, 'uniformes/ordenarMujer.html', {'uniformform':formset})


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

