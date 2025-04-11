
import sqlite3

# Función para inicializar la base de datos
def inicializar_base_datos():
    conexion = sqlite3.connect("matriculas.db")
    cursor = conexion.cursor()

    # Crear tabla si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS matriculas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            matricula TEXT UNIQUE,
            anio INTEGER,
            tipo_alumno INTEGER,
            carrera INTEGER,
            numero_alumno INTEGER
        )
    """)
    conexion.commit()
    conexion.close()

# Función para insertar datos en la base de datos
def guardar_matricula(matricula, anio, tipo_alumno, carrera, numero_alumno):
    conexion = sqlite3.connect("matriculas.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            INSERT INTO matriculas (matricula, anio, tipo_alumno, carrera, numero_alumno)
            VALUES (?, ?, ?, ?, ?)
        """, (matricula, anio, tipo_alumno, carrera, numero_alumno))
        conexion.commit()
    except sqlite3.IntegrityError:
        print("La matrícula ya existe en la base de datos.")
    finally:
        conexion.close()