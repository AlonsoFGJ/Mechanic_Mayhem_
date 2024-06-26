from django.urls import path, include
from .views import *
from rest_framework import routers # type: ignore

# CONFIGURACION PARA EL API
router = routers.DefaultRouter()
router.register('tipoempleados', TipoEmpleadoViewset)
router.register('genero', GeneroViewset)
router.register('empleados', EmpleadoViewset)

#CONFIGURAMOS LAS URL DE API
router = routers.DefaultRouter()
router.register('empleados', EmpleadoViewset)
router.register('generos', GeneroViewset)
router.register('tipoempleados', TipoEmpleadoViewset)

urlpatterns = [
    path('', index, name="index"),
    path('empleados/', empleados, name="empleados"),
    path('empleados/add/', empleadosadd, name="empleadosadd"),
    path('empleados/update/<id>/', empleadosupdate, name="empleadosupdate"),
    path('empleados/delete/<id>/', empleadosdelete, name="empleadosdelete"),
    path('categoria/categorias/', categoriacategorias, name="categoriacategorias"),
    path('categoria/ultimos_trabajos/', ultimos_trabajos, name="ultimos_trabajos"),
    path('categoria/subir_proyecto/', subir_proyecto, name="subir_proyecto"),
    path('categoria/aceptar_denegar/', aceptar_denegar, name="aceptar_denegar"),
    path('productos/', venta_productos, name="venta_productos"),
    path('account_locked/', account_locked, name="account_locked"),

    #REGISTER
    path('register/', register, name="register"),

    # API
    path('api/', include(router.urls)),
    path('empleadosapi/', empleadosapi, name="empleadosapi"),
    path('empleadodetalle/<id>/', empleadodetalle, name="empleadodetalle"),

    
]