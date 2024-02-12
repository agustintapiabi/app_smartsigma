from django.contrib import admin
from .models import Area, Proceso, Inventario, InventarioABC, HistoricoVenta

# Register your models here.

admin.site.register(Area)
admin.site.register(Proceso)
admin.site.register(Inventario)
admin.site.register(InventarioABC)
admin.site.register(HistoricoVenta)