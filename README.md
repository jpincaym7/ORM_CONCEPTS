# ORM_CONCEPTS_DJANGO
# ORM: Mapeo Objeto-Relacional (Sentencias | CRUD |)

Este repositorio contiene un conjunto de scripts y funciones para trabajar con un sistema de gestión educativa utilizando Django y un ORM (Mapeo Objeto-Relacional) para la manipulación de datos en la base de datos.

## Contenido

- `core.models`: Contiene los modelos de datos para el sistema educativo, incluyendo Periodo, Nota, DetalleNota, Estudiante, Profesor, Asignatura, y funciones auxiliares de gestión.
- `create.py`: Scripts para crear y poblar la base de datos con datos iniciales.
- `consults.py`: Funciones para realizar consultas generales en la base de datos.

## Uso

1. **Crear Registros Iniciales:**
   - Utiliza `create_bulks(state)` para crear múltiples registros eficientemente en la base de datos. Asegúrate de pasar `state=True` para habilitar la creación.

2. **Crear Notas:**
   - Utiliza `note_create(state)` para crear notas asociadas a períodos, profesores y asignaturas. Asegúrate de pasar `state=True` para habilitar la creación.

3. **Crear Detalles de Nota:**
   - Utiliza `create_detail(state)` para crear detalles de notas para cada estudiante. Asegúrate de pasar `state=True` para habilitar la creación.

4. **Consultas Generales:**
   - Utiliza `consult_basic()` para realizar consultas generales en la base de datos. Este método proporciona consultas predefinidas para estudiantes, profesores, asignaturas y notas.

## Requisitos

- Python 3.x
- Django
- Acceso a una base de datos PostgreSQL u otro motor compatible con Django.

## Ejecución

1. Clona el repositorio en tu máquina local.
2. Configura tu entorno virtual e instala las dependencias con `pip install -r requirements.txt`.
3. Asegúrate de tener configurada una base de datos compatible con Django y ajusta la configuración en `settings.py`.
4. Ejecuta los scripts según sea necesario, y realiza consultas utilizando las funciones proporcionadas en `consults.py`.

---

¡Disfruta explorando y desarrollando con tu sistema de gestión educativa!
