# Hola Marbel

Proyecto Django pequeño organizado con arquitectura hexagonal.

## Ejecutar

En PowerShell, desde esta carpeta:

```powershell
.\.venv\Scripts\Activate.ps1
python manage.py migrate
python manage.py runserver
```

Abre http://127.0.0.1:8000/ para ver el saludo.

## Estructura

- `domain`: modelo del dominio.
- `application/ports`: contrato del caso de uso.
- `application/services`: implementacion del saludo.
- `infrastructure/web`: adaptador HTTP, rutas y plantilla.
- `infrastructure/settings.py`: configuracion de Django.# 