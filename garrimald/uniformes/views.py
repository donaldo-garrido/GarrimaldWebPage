from django.shortcuts import render
#from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory
#from .models import Pizza, Size
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView



def home(request):
    return render(request, 'uniformes/home.html')

def administradores(request):
    return render(request, 'uniformes/administradores.html')