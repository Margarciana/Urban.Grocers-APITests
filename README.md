# Proyecto Urban Grocers 
El presente proyecto integra las funciones y pruebas necesarias para ejecutar la lista de comprobación dirigida específicamente al campo 'name' en la creación de kits, de la aplicación Urban.Grocers;
el objetivo es probar los rangos y clases de equivalencia. 

## Estructura del Proyecto

- **configuration.py:** Contiene las URLs y rutas de solicitud
- **data.py:** Almacena los cuerpos de las solicitudes POST
- **sender_stand_request.py:** Funciones para enviar las solicitudes HTTP
- **create_kit_name_kit_test.py:** Archivo principal con todas las pruebas
- **README.md:** Documentación del proyecto
- **.gitignore:** Especifica qué archivos ignorar en el control de versiones

## Configuración del Proyecto
### 1. Configurar configuration.py
python
URL_SERVICE = "https://tu-servidor-urban-grocers.com"
CREATE_USER_PATH = "/api/v1/users/"
KITS_PATH = "/api/v1/kits/"

### 2. Configurar data.py
```python
user_body = {
    "firstName": "Andrea", 
    "phone": "+11234567890",
    "address": "123 Elm Street, 14"
}

kit_body = {
    "name": "Mi kit"
}
```

### 3. Configurar sender_stand_request.py
```python
import configuration
import requests
import data

# Funciones para enviar solicitudes HTTP
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body)

# Ejemplo de función completa
def post_new_kit(kit_body, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, 
                        json=kit_body, headers=headers)
```

### 4. Instalar dependencias

pip install requests pytest

### 5. Ejecución de Pruebas
pytest create_kit_name_kit_test.py -v

### 6. Estructura de imports en create_kit_name_kit_test.py
``` python
import data
import sender_stand_request
from data import get_kit_body, name_1_char, name_with_spaces, name_numbers, name_0_chars, \ 
    name_512_chars, kit_body_no_name, name_511_chars, name_special_chars, kit_body_number_name
```

## Fuente
https://cnt-f4311f80-4bff-4258-a320-703bcbbf4b72.containerhub.tripleten-services.com/docs/

## Tecnologías y Técnicas utilizadas

- **Python:** Lenguaje de programación utilizado
- **Pytest:** Framework para ejecutar las pruebas  
- **requests:** Biblioteca para hacer peticiones HTTP
- **Pruebas de API:** Técnica utilizada para validar endpoints
- **Métodos HTTP:** GET, POST, PUT, DELETE
