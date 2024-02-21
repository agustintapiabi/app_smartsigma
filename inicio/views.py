from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.paginator import Paginator
from collections import defaultdict
from django.db.models.functions import ExtractYear
from datetime import datetime
from .models import Proceso, Inventario, HistoricoVenta, VentasPorMes
from .forms import AñadirProceso, AñadirSKU, IngresarVenta
from django.http.response import JsonResponse

# Se establece conexion con los Archivos HTML
# Se crean las funciones que hacen a las Aplicaciones

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('indexsoftware')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'La contraseña o el usuario es incorrecto'
            })
        else:
            login(request, user)
            return redirect('indexsoftware')

@login_required
def signout(request):
    logout(request)
    return redirect('signin')

def about(request):
    return render(request, 'about.html')


# Funciones Tecnicas de la Aplicacion

@login_required
def indexsoftware(request):
    return render(request, '0. Home/index-software.html')

@login_required
def seguimiento(request):
    return render(request, '0. Home/seguimiento.html')

@login_required
def ingresardatos(request):
    if request.method == 'POST':
       if request.POST.get('sku') and request.POST.get('cantidad') and request.POST.get('precio') and request.POST.get('fecha'):
            venta = HistoricoVenta()
            venta.SKU = request.POST.get('sku')
            venta.Cantidad = request.POST.get('cantidad')
            venta.Precio = request.POST.get('precio')
            venta.Fecha = request.POST.get('fecha')
            venta.save()
            return render(request, '0. Home/ingresardatos.html')
    else:
       return render(request, '0. Home/ingresardatos.html')

@login_required
def modificardatos(request, id):
    if request.method == 'GET':
        SKU = get_object_or_404(HistoricoVenta, id=id)
        form = IngresarVenta(instance=SKU)
        return render(request, '0. Home/modificardatos.html', {
            'SKU': SKU,
            'form': form
        })
    else:
        try:
            SKU = get_object_or_404(HistoricoVenta, id=id)
            form = IngresarVenta(request.POST, instance=SKU)
            form.save()
            return redirect('historicoventas')
        except ValueError:
            return render(request, '0. Home/modificardatos.html', {
            'SKU': SKU,
            'form': form,
            'error': 'No se pudo actualizar'
        })

@login_required
def eliminardatos(request, id):
    SKU = get_object_or_404(HistoricoVenta, id=id)
    if request.method == 'POST':
        SKU.delete()
        return redirect('historicoventas')



@login_required
def Procesos(request):
    Procesos = Proceso.objects.all()
    return render(request, 'Gestion de Procesos/procesos.html', {
        'Procesos': Procesos
    })

@login_required
def AñadirProcesos(request):
    if request.method == 'GET':
        return render(request, 'Gestion de Procesos/añadir_proceso.html', {
            'form': AñadirSKU
        })
    else:
        try:
            form = AñadirProceso(request.POST)
            nuevo_proceso = form.save(commit=False)
            nuevo_proceso.save()
            return redirect('procesos')
        except ValueError:
            return render(request, 'Gestion de Procesos/añadir_proceso.html', {
            'form': AñadirProceso,
            'error': 'No es valido'
        })

@login_required
def Inventarios(request):
    Inventarios = Inventario.objects.all()
    return render(request, 'Gestion de Inventario/inventario.html', {
        'Inventarios': Inventarios
    })

@login_required
def AñadirSKUs(request):
    if request.method == 'GET':
        return render(request, 'Gestion de Inventario/añadir_sku.html', {
            'form': AñadirSKU
        })
    else:
        try:
            form = AñadirSKU(request.POST)
            nuevo_sku = form.save(commit=False)
            nuevo_sku.save()
            return redirect('inventario')
        except ValueError:
            return render(request, 'Gestion de Inventario/añadir_sku.html', {
            'form': AñadirSKU,
            'error': 'No es valido'
        })

@login_required
def DetalleSKU(request, id):
    if request.method == 'GET':
        SKU = get_object_or_404(Inventario, id=id)
        form = AñadirSKU(instance=SKU)
        return render(request, 'Gestion de Inventario/detalle_sku.html', {
            'SKU': SKU,
            'form': form
        })
    else:
        try:
            SKU = get_object_or_404(Inventario, id=id)
            form = AñadirSKU(request.POST, instance=SKU)
            form.save()
            return redirect('inventario')
        except ValueError:
            return render(request, 'Gestion de Inventario/detalle_sku.html', {
            'SKU': SKU,
            'form': form,
            'error': 'No se pudo actualizar'
        })

@login_required
def EliminarSKU(request, id):
    SKU = get_object_or_404(Inventario, id=id)
    if request.method == 'POST':
        SKU.delete()
        return redirect('inventario')

@login_required
def HistoricoVentas(request):
    historicoventas = HistoricoVenta.objects.order_by('-Fecha')
    paginator = Paginator(historicoventas, 20)  # Divide las ventas en páginas, con 10 ventas por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, '1. Planificacion de la Demanda/historico_ventas.html', {'page_obj': page_obj})

def VentasPorMesView(request):
    historicoventas = HistoricoVenta.objects.order_by('-Fecha')
    ventas_por_mes = calcular_ventas_por_mes(historicoventas)
    numeros_meses = range(1, 13)
    # Obtener años únicos disponibles en la base de datos
    available_years = HistoricoVenta.objects.annotate(year=ExtractYear('Fecha')).values_list('year', flat=True).distinct()
    selected_year = request.GET.get('year')
    # Si no se selecciona un año, mostrar el último año por defecto
    if not selected_year:
        selected_year = available_years[0] if available_years else None
    # Filtrar ventas por el año seleccionado
    if selected_year:
        historicoventas = historicoventas.filter(Fecha__year=selected_year)
        ventas_por_mes = calcular_ventas_por_mes(historicoventas)
    # Crear una lista de tuplas de la forma (año, [cantidad_ventas_mes1, cantidad_ventas_mes2, ...])
    datos_tabla = []
    for año, meses in ventas_por_mes.items():
        cantidad_ventas_por_mes = [meses.get(num_mes, 0) for num_mes in numeros_meses]
        datos_tabla.append((año, cantidad_ventas_por_mes))
    return render(request, '1. Planificacion de la Demanda/ventas_por_mes.html', {'datos_tabla': datos_tabla, 'numeros_meses': numeros_meses, 'available_years': available_years, 'selected_year': selected_year})

def calcular_ventas_por_mes(historicoventas):
    ventas_por_mes = defaultdict(dict)
    for venta in historicoventas:
        mes = venta.Fecha.month
        año = venta.Fecha.year
        if año not in ventas_por_mes:
            ventas_por_mes[año] = {}
        ventas_por_mes[año][mes] = ventas_por_mes[año].get(mes, 0) + 1
    return ventas_por_mes