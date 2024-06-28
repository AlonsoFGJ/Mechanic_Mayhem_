import datetime
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from .serializers import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group 
#IMPORT API
from rest_framework import viewsets # type: ignore
from rest_framework.renderers import JSONRenderer # type: ignore
import requests # type: ignore
from django.core.paginator import Paginator


# Create your views here.
def user_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

def group_required(group_name):
    def decorator(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if user_in_group(request.user, group_name):
                return view_func(request,*args, **kwargs)
            else:
                messages.error(request, 'No tienes permisos para acceder a la página')
                return redirect(to='index')
        return _wrapped_view
    return decorator

#PROBLEMA AL AGREGAR USUARIOS SALTA PROBLEMA DE QUERY PERO SI FUNCIONA
def register (request): 
    aux = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            user = formulario.save()
            group = Group.objects.get(name='Cliente')
            user.groups.add(group)

            messages.success(request, "Usuario creado correctamente")
            return redirect(to="empleados")
        else: 
            aux['form'] = formulario

    return render(request, 'core/registration/register.html', aux)

def index (request):
    return render(request, 'core/index.html')

def account_locked (request):
    return render(request, 'core/cuentas/account_locked.html')

@permission_required('core.view_empleado')
def empleados (request): 

    empleados = Empleado.objects.all()

    #Paginator
    paginator = Paginator(empleados,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    aux = {
        'lista' : empleados,
        'page_obj' : page_obj
    }

    return render(request, 'core/empleados/index.html', aux)

@permission_required('core.add_empleado')
def empleadosadd(request):
    aux = {
        'form': EmpleadoForm()
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            empleado = formulario.save(commit=False)
            empleado.save()
            messages.success(request, "Mecánico/a creado/a correctamente")
            return redirect('empleados')
        else:
            aux['form'] = formulario
            messages.error(request, "El Mecánico/a no se pudo crear!")

    return render(request, 'core/empleados/crud/add.html', aux)

@permission_required('core.change_empleado')
def empleadosupdate (request, id):
    empleado = Empleado.objects.get(id=id)
    aux = {
        'form' : EmpleadoForm(instance=empleado)
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST, instance=empleado, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request, "Mecanico/a  modificado/a  correctamente")
        else: 
            aux['form'] = formulario
            messages.error(request, "Error al modificar Mecanico/a !")

    return render(request, 'core/empleados/crud/update.html', aux)

@permission_required('core.delete_empleado')
def empleadosdelete (request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()

    return redirect(to="empleados")

@group_required('Mecanico') 
def aceptar_denegar (request):
    aux2 = {
        'form' : SubirProyectoForm()
    }
    
    if request.method == 'POST':
        formulario = SubirProyectoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Subiste un proyecto correctamente.")
        else:
            aux2['form'] = formulario
            messages.error(request, "Error al subir el proyecto.")

    return render(request, 'core/categoria/aceptar_denegar.html', aux2)

def categoriacategorias (request):
    return render(request, 'core/categoria/categorias.html')

@group_required('Gerente') 
def subir_proyecto(request):
    proyectos = SubirProyecto.objects.all()
    aux2 = {
        'lista2': proyectos
    }

    return render(request, 'core/categoria/subir_proyecto.html', aux2)

def ultimos_trabajos (request):
    return render(request, 'core/categoria/ultimos_trabajos.html')

@permission_required('core.view_empleado')
def venta_productos(request):
    # Aquí podrías agregar lógica adicional, como procesamiento de compra

    if request.method == 'POST':
        # Ejemplo ficticio de procesamiento de compra
        compra_exitosa = True  # Simulación de una compra exitosa (cambiar según lógica real)

        if compra_exitosa:
            messages.success(request, "Gracias por tu compra")
        else:
            messages.error(request, "Error al procesar compra, inténtalo más tarde")

    return render(request, 'core/venta/productos.html')



# UTILIZAMOS LAS VIEWSET PARA MANEJAR LAS PETICIONES HTTP (GET,POST,PUT,DELETE)
class TipoEmpleadoViewset(viewsets.ModelViewSet):
    queryset = TipoEmpleado.objects.all().order_by('id')
    serializer_class = TipoEmpleadoSerializers
    renderer_classes = [JSONRenderer]

class EmpleadoViewset(viewsets.ModelViewSet):
    queryset = Empleado.objects.all().order_by('id')
    serializer_class = EmpleadoSerializers
    renderer_classes = [JSONRenderer]

class GeneroViewset(viewsets.ModelViewSet):
    queryset = Genero.objects.all().order_by('id')
    serializer_class = GeneroSerializers
    renderer_classes = [JSONRenderer]

def empleadosapi (request): 
    response = requests.get('http://127.0.0.1:8000/api/empleados/')
    empleados = response.json()

    paginator = Paginator(empleados,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    aux = {
        'lista' : empleados,
        'page_obj' : page_obj
    }

    return render(request, 'core/empleados/crudapi/index.html', aux)
    
def empleadodetalle(request, id):
    response = requests.get(f'http://127.0.0.1:8000/api/empleados/{id}/')
    empleado = response.json()

    # Construye la URL absoluta de la imagen
    if empleado.get('imagen'):
        empleado['imagen'] = f'http://127.0.0.1:8000/{empleado["imagen"]}'

    aux = {
        'empleado': empleado
    }

    return render(request, 'core/empleados/crudapi/detalle.html', aux)