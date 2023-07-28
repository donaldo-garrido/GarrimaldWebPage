# Importamos las librerías necesarias
from django.shortcuts import render
from django.forms import formset_factory
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
import pandas as pd
import numpy as np

# Importamos funciones y clases
from .forms import HombreForm, MujerForm
from .models import Pedidos, Precios

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

            cantidades = [created_uni.escuela_id, created_uni.sueter_mujer_cantidad, created_uni.sueter_hombre_cantidad, 
                   created_uni.jumper_cantidad, created_uni.pantalon_cantidad, created_uni.blusa_cantidad,
                   created_uni.camisa_cantidad, created_uni.chamarra_cantidad, created_uni.pants_cantidad,
                   created_uni.playera_cantidad, created_uni.bordados]
            
            tallas = [created_uni.escuela_id, created_uni.sueter_mujer, created_uni.sueter_hombre, 
                   created_uni.jumper, created_uni.pantalon, created_uni.blusa,
                   created_uni.camisa, created_uni.chamarra, created_uni.pants,
                   created_uni.playera, '']
            
            
            list_finalizar, suma = Calculations(cantidades, tallas)
            

            print(created_uniform_pk)
            print(created_uni.nombre)

            instance = {'created_uniform_pk':created_uniform_pk, 'dict_finalizar':list_finalizar, 'suma':suma}
            
        return render(request, 'uniformes/finalizar.html', instance)
    else: return render(request, 'uniformes/ordenarMujer.html', {'uniformform':formset})


# -----------------------------------------------
# Función para calcular el costo de un pedido
def Calculations(cantidades, tallas):

    list_fin = []
    preciosDB = Precios.objects.get(pk=cantidades[0])
    print(preciosDB)
    print('........................................')

    titulos = ['Escuela', 'Sueter (M)', 'Sueter (H)', 'Jumper', 
               'Pantalon', 'Blusa', 'Camisa', 'Chamarra', 'Pants', 
               'Playera', 'Bordados']
    
    precios = [preciosDB.escuela_id, preciosDB.sueter_mujer_cantidad, preciosDB.sueter_hombre_cantidad, 
                   preciosDB.jumper_cantidad, preciosDB.pantalon_cantidad, preciosDB.blusa_cantidad,
                   preciosDB.camisa_cantidad, preciosDB.chamarra_cantidad, preciosDB.pants_cantidad,
                   preciosDB.playera_cantidad, preciosDB.bordados]
    
    totales = np.array(cantidades)*np.array(precios)
    print(len(cantidades), len(titulos), len(precios))
    print('........................................')
    print(cantidades)
    print('........................................')
    print(titulos)
    print('........................................')
    print(precios)
    print('........................................')
    print(totales)

    suma = 0

    for item in range(len(totales)-1):
        if totales[item+1] != 0.0:
            
            if item+2 == len(totales):
                prenda = titulos[item+1]
            else: prenda = titulos[item+1]+' T-'+str(tallas[item+1])
            dict_finalizar = {'prenda':prenda,'cantidad':cantidades[item+1],
                                  'precio':precios[item+1], 'total':totales[item+1]}
                
            list_fin.append(dict_finalizar)
            suma += totales[item+1]

    
    return list_fin, suma


# -----------------------------------------------
# Función para ordenar un pedido de niño
# Orden:
# Sueter, jumper, pantalon, blusa, camisa, chamarra, pants, playera, bordados
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
def editar(request, pk, sexo):
    pedido = Pedidos.objects.get(pk=pk)
    if sexo == 'Mujer':
        form = MujerForm(instance=pedido)

        if request.method == 'POST':
            filled_form = MujerForm(request.POST, instance=pedido)
            if filled_form.is_valid():
                filled_form.save()
                form = filled_form
                note = 'El pedido fue actualizado'
                return render(request, 'uniformes/finalizar.html', {'created_uniform_pk':created_uniform_pk, 'dict_finalizar':list_finalizar, 'note':note})

    elif sexo == 'Hombre':
        form = HombreForm(instance=pedido)

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

