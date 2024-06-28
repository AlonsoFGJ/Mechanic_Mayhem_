from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework import routers
from .views import *

# Configuración para el API
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

    # REGISTER
    path('register/', register, name="register"),

    # API URLs
    path('api/', include(router.urls)),  # URLs generadas por el router de DRF
    path('empleadosapi/', empleadosapi, name="empleadosapi"),  # Ejemplo de una vista de API específica
    path('empleadodetalle/<id>/', empleadodetalle, name="empleadodetalle"),  # Vista de detalle de empleado

    # URLs de autenticación de Django
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
