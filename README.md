# Proyecto Urban Grocers 
El presente proyecto integra las funciones y pruebas necesarias para ejecutar la lista de comprobación dirigida específicamente al campo 'name' en la creación de kits, de la aplicación Urban.Grocers; el objetivo es probar los rangos y clases de equivalencia ejecutando esta suite automatizada. 
Urban.Grocers es una plataforma de delivery de insumos bajo demanda.

## **Técnicas y tecnologías empleadas:**
#### - **GitBash:** Para clonar la plantilla del repositorio a mi pc.
#### - **Python:** Lenguaje utilizado para la redacción del código.
#### - **PyCharm:** Desarrollo del código.
#### - **PyTest:** Gestión y automatización de pruebas de software.

## 🚀 Instrucciones de Ejecución

Para clonar y ejecutar estas pruebas en tu entorno local, sigue estos pasos:

### 1. Requisitos Previos
```bash
- Python 3.x instalado.
- PyCharm (o tu IDE preferido).
```
### 2. Instalación de Dependencias
Abre la terminal en la raíz del proyecto y ejecuta:
```bash
pip install requests pytest
```
### 3. Configuración del Servidor / URL Base
Asegúrate de actualizar la variable URL_SERVICE en el archivo configuration.py con la URL activa del servidor de pruebas:
```bash
URL_SERVICE = "[https://tu-servidor-de-pruebas.serverhub.tripleten-services.com](https://tu-servidor-de-pruebas.serverhub.tripleten-services.com)"
```
### 4. Ejecución de las Pruebas
```bash
pytest create_kit_name_kit_test.py
```
## Fuente
https://cnt-f4311f80-4bff-4258-a320-703bcbbf4b72.containerhub.tripleten-services.com/docs/

- **Pruebas de API:** Técnica utilizada para validar endpoints
- **Métodos HTTP:** GET, POST, PUT, DELETE
