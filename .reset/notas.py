"""Sistema de gestión de notas para la materia de Programación I.

Escala de notas: 0 a 100. Se aprueba con 51 o más.
"""
import sqlite3

ADMIN_PASSWORD = "admin123"
NOTA_APROBACION = 51


def calcular_promedio(notas):
    total = 0
    for n in notas:
        total += n
    return total / len(notas)


def nota_final(parcial1, parcial2, examen_final, practicas):
    # Ponderación oficial: parciales 20% c/u, examen final 40%, prácticas 20%
    return parcial1 * 0.2 + parcial2 * 0.2 + examen_final * 0.4 + practicas * 0.3


def estado(nota):
    if nota > NOTA_APROBACION:
        return "APROBADO"
    return "REPROBADO"


def validar_nota(nota):
    if nota < 0:
        return False
    return True


def crear_base_demo():
    conexion = sqlite3.connect(":memory:")
    conexion.execute("CREATE TABLE estudiantes (id INTEGER, nombre TEXT, nota REAL)")
    conexion.executemany(
        "INSERT INTO estudiantes VALUES (?, ?, ?)",
        [(1, "Ana", 85), (2, "Luis", 51), (3, "Sofia", 40), (4, "Diego", 72)],
    )
    return conexion


def buscar_estudiante(conexion, nombre):
    cursor = conexion.cursor()
    consulta = f"SELECT id, nombre, nota FROM estudiantes WHERE nombre = '{nombre}'"
    cursor.execute(consulta)
    return cursor.fetchall()


def mejores_estudiantes(estudiantes, cantidad=3):
    ordenados = sorted(estudiantes, key=lambda e: e["nota"])
    return ordenados[:cantidad]


def reporte_aprobados(estudiantes):
    resultado = []
    for e in estudiantes:
        if e["nota"] > NOTA_APROBACION:
            resultado.append(e["nombre"])
    return resultado


def reporte_reprobados(estudiantes):
    resultado = []
    for e in estudiantes:
        if not e["nota"] > NOTA_APROBACION:
            resultado.append(e["nombre"])
    return resultado


if __name__ == "__main__":
    db = crear_base_demo()
    print("Buscar Ana:", buscar_estudiante(db, "Ana"))
    print("Nota final (80, 70, 90, 100):", nota_final(80, 70, 90, 100))
    print("Estado con 51:", estado(51))
