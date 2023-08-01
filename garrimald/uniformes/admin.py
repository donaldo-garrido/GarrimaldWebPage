from django.contrib import admin
from .models import Escuela, Pedidos, Precios, Total

# Register your models here.
admin.site.register(Escuela)
admin.site.register(Pedidos)
admin.site.register(Precios)
admin.site.register(Total)
#admin.site.register()