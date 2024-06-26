import os
import sys

from django.core.wsgi import get_wsgi_application

# Añadir el directorio actual al sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Ajustar el nombre del módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pagina.settings")

# Configuración de Django
application = get_wsgi_application()

# Opcional: Asignar app a application
app = application