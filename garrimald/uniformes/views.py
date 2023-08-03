# Importamos las librerías necesarias
from django.shortcuts import render
from django.forms import formset_factory
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
import pandas as pd
import numpy as np

# Importamos funciones y clases
from .forms import HombreForm, MujerForm, CuentaForm, VerForm, SexoForm
from .models import Pedidos, Precios, Total

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

    sexoform = SexoForm()

    if request.method == 'POST':
        sexoform = SexoForm(request.POST)
        if sexoform.is_valid():
            pk_pedido = filled_form.cleaned_data.get('sexo')
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

            total_pedido = Total(pedido=created_uniform_pk, total=suma)
            total_pedido.save()

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
# Función para editar un pedido
@login_required(login_url='login')
def editarMujer(request, pk):
    pedido = Pedidos.objects.get(pk=pk)

    form = MujerForm(instance=pedido)

    if request.method == 'POST':
        filled_form = MujerForm(request.POST, instance=pedido)
        if filled_form.is_valid():
            created_uni = filled_form.save()
            form = filled_form
            note = 'El pedido fue actualizado'
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

            total_pedido = Total(pedido=created_uniform_pk, total=suma)
            total_pedido.save()

            instance = {'created_uniform_pk':created_uniform_pk, 'dict_finalizar':list_finalizar, 'suma':suma, 'nombre': created_uni.nombre}
            
        return render(request, 'uniformes/finalizar.html', instance)
            
    return render(request, 'uniformes/editarMujer.html', {'uniformform':form, 'pedido':pedido})

# -----------------------------------------------
# Función para 
@login_required(login_url='login')
def pagar(request, pk):

    pago = Total.objects.get(pk=pk)

    form = CuentaForm(instance=pago)

    if request.method == 'POST':
        filled_form = CuentaForm(request.POST, instance=pago)
        if filled_form.is_valid():
            created_pago = filled_form.save()
            form = filled_form

            resta = pago.total-created_pago.a_cuenta

            #resta_pedido = Total(resta=resta, entregado=0)
            #resta_pedido.save()
            pago.resta = resta
            pago.save()
            #instance = {'created_uniform_pk':created_uniform_pk, 'dict_finalizar':list_finalizar, 'suma':suma, 'nombre': created_uni.nombre}
            
            return render(request, 'uniformes/pagar.html', {'pagoform':form, 'resta':resta, 'pedido_pk':pk})
            
    return render(request, 'uniformes/pagar.html', {'pagoform':form, 'pedido_pk':pk})



    return render(request, 'uniformes/pagar.html')

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

# -----------------------------------------------
# Función para ver un pedido (externo)

def ver(request):
    filled_form = VerForm()
    if request.method == 'POST':
        filled_form = VerForm(request.POST)
        if filled_form.is_valid():
            pk_pedido = filled_form.cleaned_data.get('ver_pk')

            celular = filled_form.cleaned_data.get('celular')

            info = Pedidos.objects.get(pk=pk_pedido)
            dinero = Total.objects.get(pk=pk_pedido)

            if celular == info.celular:

                data = tabular(pk_pedido)

                detalles = {}

                detalles['nombre'] = info.nombre
                detalles['escuela'] = info.escuela
                detalles['fecha'] = info.fecha_hora[:10]
                detalles['bordados'] = info.bordados
                detalles['total'] = dinero.total
                detalles['a_cuenta'] = dinero.a_cuenta
                detalles['resta'] = dinero.resta
                if dinero.entregado == 0:
                    detalles['entregado'] = 'No'
                else: detalles['entregado'] = 'Sí'

                return render(request, 'uniformes/ver.html', {'verform':filled_form, 'data':data, 'detalles':detalles})


            else: 
                note = 'El número celular no coincide con el proporcionado al hacer el pedido. \nIntente de nuevo.'
                filled_form = VerForm()
                return render(request, 'uniformes/ver.html', {'verform':filled_form, 'note':note,})

        
    else: return render(request, 'uniformes/ver.html', {'verform':filled_form})

# -----------------------------------------------
# Función para sacar diccionario para tabular
def tabular(pk_pedido):

    list_fin = []
    data = Pedidos.objects.get(pk=pk_pedido)

    titulos = ['Sueter (M)', 'Sueter (H)', 'Jumper', 
               'Pantalon', 'Blusa', 'Camisa', 'Chamarra', 'Pants', 
               'Playera',]
    
    cantidades = [data.sueter_mujer_cantidad, data.sueter_hombre_cantidad, 
                   data.jumper_cantidad, data.pantalon_cantidad, data.blusa_cantidad,
                   data.camisa_cantidad, data.chamarra_cantidad, data.pants_cantidad,
                   data.playera_cantidad,]

    tallas = [data.sueter_mujer, data.sueter_hombre, 
                   data.jumper, data.pantalon, data.blusa,
                   data.camisa, data.chamarra, data.pants,
                   data.playera, ]
    
    for item in range(len(cantidades)):
        cantidad = cantidades[item]
        if cantidad > 0:

            prenda = titulos[item]
            talla = tallas[item]

            dict_finalizar = {'prenda':prenda, 'talla':talla, 'cantidad':cantidad,}
                
            list_fin.append(dict_finalizar)

    return list_fin


