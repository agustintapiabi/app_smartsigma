from django.urls import path 
from . import views

# Direcciones URL que se encuentran dentro de la Aplicacion

urlpatterns = [
    path('', views.index, name="index"),
    path('SignUp/', views.signup, name="signup"),
    path('SignIn/', views.signin, name="signin"),
    path('LogOut/', views.signout, name="logout"),
    path('About/', views.about, name="about"),
    path('Inicio/', views.indexsoftware, name="indexsoftware"),
    path('Inicio/seguimiento', views.seguimiento, name="seguimiento"),
    path('Inicio/ingresardatos', views.ingresardatos, name="ingresardatos"),
    path('Inicio/modificardatos/<int:id>', views.modificardatos, name="modificardatos"),
    path('Inicio/ingresardatos/<int:id>/delete', views.eliminardatos, name="eliminardatos"),
    path('Inicio/historicoventas', views.HistoricoVentas, name="historicoventas"),
    path('Procesos/', views.Procesos, name="procesos"),
    path('añadir_proceso/', views.AñadirProcesos, name="añadir_proceso"),
    path('Inicio/inventario', views.Inventarios, name="inventario"),
    path('Inventario/<int:id>', views.DetalleSKU, name="detalle_sku"),
    path('Inventario/<int:id>/delete', views.EliminarSKU, name="eliminar_sku"),
    path('añadir_sku/', views.AñadirSKUs, name="añadir_sku"),
]
