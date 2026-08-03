# API CRUD Automation Testing

Proyecto de automatización de pruebas para APIs REST utilizando **Python**, **Pytest** y la librería **Requests**.

El objetivo del proyecto es practicar el consumo de APIs, la validación de respuestas HTTP y la automatización de pruebas sobre operaciones CRUD utilizando la API pública **ReqRes**.

---

## Tecnologías utilizadas

- Python 3.x
- Pytest
- Requests
- PyCharm

---

## Funcionalidades cubiertas

Se automatizaron pruebas para los siguientes endpoints:

| Método | Endpoint | Descripción |
|---------|----------|-------------|
| GET | `/api/users?page={page}` | Obtener lista de usuarios |
| GET | `/api/users/{id}` | Obtener un usuario específico |
| POST | `/api/users` | Crear un usuario |
| PUT | `/api/users/{id}` | Actualizar completamente un usuario |
| PATCH | `/api/users/{id}` | Actualizar parcialmente un usuario |
| DELETE | `/api/users/{id}` | Eliminar un usuario |

---

## Validaciones realizadas

Las pruebas incluyen validaciones como:

- Código de estado HTTP
- Tiempo de respuesta
- Campos obligatorios del JSON
- Tipos de datos
- Comparación entre el payload enviado y la respuesta obtenida
- Validación de encabezados HTTP
- Validación del contenido del body

---

## Estructura del proyecto

```
API CRUD/
│
├── api/
│   └── users_api.py
│
├── tests/
│   └── test_users.py
│
├── config.py
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Instalación

Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual.

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución de las pruebas

Ejecutar todas las pruebas:

```bash
pytest
```

Mostrar la salida de `print()`:

```bash
pytest -s
```

Ejecutar una prueba específica:

```bash
pytest tests/test_users.py
```

---

## Aprendizajes obtenidos

Durante el desarrollo de este proyecto se practicaron conceptos como:

- Consumo de APIs REST
- Métodos HTTP (GET, POST, PUT, PATCH y DELETE)
- Interpretación de respuestas JSON
- Uso de parámetros de ruta y parámetros de consulta
- Construcción de payloads
- Diseño de casos de prueba positivos y negativos
- Organización de un proyecto de automatización con Pytest

---

## API utilizada

El proyecto utiliza la API pública de **ReqRes**, diseñada para practicar pruebas y consumo de servicios REST.

https://reqres.in

---

## Autor

Daniel Arteaga