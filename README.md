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

## Probar con Postman Web

1. Inicia Django con `python manage.py runserver`.
2. En Postman Web, importa el archivo `postman_collection.json` desde **Import**.
3. Selecciona **Desktop Agent** para que Postman pueda conectarse al servidor local.
4. Abre la solicitud **Obtener saludo** y pulsa **Send**.

La respuesta es HTML. Postman Web no aloja este proyecto; la solicitud usa el servidor local de tu computadora.

## Estructura

- `domain`: modelo del dominio.
- `application/ports`: contrato del caso de uso.
- `application/services`: implementacion del saludo.
- `infrastructure/web`: adaptador HTTP, rutas y plantilla.
- `infrastructure/settings.py`: configuracion de Django.# 