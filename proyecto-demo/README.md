# Proyecto demo: gestión de notas

Este proyecto reúne funciones de ejemplo para calcular promedios y notas finales, validar calificaciones y determinar si un estudiante aprueba. También permite consultar una base SQLite temporal con estudiantes de demostración, ordenar estudiantes por nota y generar listas de aprobados y reprobados.

## Requisitos

- Python 3. No requiere paquetes externos: utiliza módulos de la biblioteca estándar (`os`, `sqlite3` y `unittest`).

## Estructura

```text
proyecto-demo/
├── notas.py
├── README.md
└── tests/
    └── test_notas.py
```

## Funciones de `notas.py`

| Nombre | Parámetros | Qué devuelve |
|---|---|---|
| `calcular_promedio` | `notas`: lista de calificaciones | El promedio como número. Lanza `ValueError` si la lista está vacía. |
| `nota_final` | `parcial1`, `parcial2`, `examen_final`, `practicas`: calificaciones | La suma ponderada como número. |
| `estado` | `nota`: calificación | `"APROBADO"` si la nota es al menos 51; de lo contrario, `"REPROBADO"`. |
| `validar_nota` | `nota`: valor que se desea validar | `True` si es un entero o decimal entre 0 y 100, inclusive; si no, `False`. |
| `crear_base_demo` | Ninguno | Una conexión SQLite en memoria con la tabla `estudiantes` y cuatro registros de ejemplo. |
| `buscar_estudiante` | `conexion`: conexión SQLite; `nombre`: nombre que se busca | Una lista de filas con los campos `id`, `nombre` y `nota`; puede estar vacía si no hay coincidencias. |
| `mejores_estudiantes` | `estudiantes`: lista de diccionarios con `nota`; `cantidad`: máximo de resultados (por defecto, `3`) | Una lista de hasta esa cantidad de estudiantes, ordenados por nota descendente. |
| `reporte_aprobados` | `estudiantes`: lista de diccionarios con `nombre` y `nota` | Una lista de nombres con nota de aprobación. |
| `reporte_reprobados` | `estudiantes`: lista de diccionarios con `nombre` y `nota` | Una lista de nombres con nota de reprobación. |

## Reglas de notas

- La escala válida va de 0 a 100, inclusive.
- La nota final se calcula con dos parciales de 20 % cada uno, el examen final de 40 % y las prácticas de 20 %.
- La nota mínima de aprobación es 51; una nota inferior se considera reprobada.

## Ejecutar la demo

Desde la carpeta `proyecto-demo`, ejecuta:

```bash
python notas.py
```

La demo busca a Ana en la base temporal, calcula una nota final de ejemplo y muestra el estado correspondiente a una nota de 51.

## Ejecutar las pruebas

Desde la carpeta `proyecto-demo`, ejecuta:

```bash
python -m unittest discover -s tests -v
```
