from django.contrib import admin
from .models import Escuela, Pedidos, Precios, Total, Cuenta, Resta

# Register your models here.
admin.site.register(Escuela)
admin.site.register(Pedidos)
admin.site.register(Precios)
admin.site.register(Total)
admin.site.register(Cuenta)
admin.site.register(Resta)
#admin.site.register()