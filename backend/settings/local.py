from .base import *

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'tramontina_compras_db',
        'USER': '',  # Usuario de SQL Server
        'PASSWORD': '',  # Contraseña de SQL Server
        'HOST': 'localhost',  # El nombre de tu servidor o IP
        #'PORT': '',  # Puerto del servidor, si es necesario (por defecto 1433)
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',  # El driver ODBC adecuado
            'Trusted_Connection' : 'yes',
        
        }
    }
}

CORS_ALLOW_ALL_ORIGINS = True  # Permitir todas las solicitudes desde el frontend
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'