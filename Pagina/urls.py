"""
URL configuration for Pagina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # URL para la app 'core'
    #path('accounts/', include('django.contrib.auth.urls')),  # URLs de autenticación de Django
    path('captcha/', include('captcha.urls')),  # URLs de Captcha,
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),  # Reset de contraseña
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),  # Confirmación de envío de reset
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # Confirmación de reset
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  # Completado de reset
]

# Configuración para servir archivos estáticos en desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)