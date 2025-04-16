import time

class GeneradorMatricula:
    def __init__(self):
        self.anio_actual = time.localtime().tm_year  # Obtiene el año actual automáticamente

    def generar_matricula(self, tipo_alumno, num_carrera, num_alumno):
        # Formatear número de alumno con ceros a la izquierda (3 dígitos)
        num_alumno_formateado = f"{num_alumno:03d}"
        return f"{self.anio_actual}{tipo_alumno}{num_carrera}{num_alumno_formateado}"
############################3

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

############################

import tkinter as tk
import sqlite3

def mostrar_datos_en_gui():
    ventana_datos = tk.Toplevel()
    ventana_datos.title("Matrículas almacenadas")
    ventana_datos.geometry("500x400")

    # Cuadro de texto para mostrar los datos
    cuadro_texto = tk.Text(ventana_datos, wrap=tk.WORD)
    cuadro_texto.pack(expand=True, fill=tk.BOTH)

    # Conectar a la base de datos y recuperar datos
    conexion = sqlite3.connect("matriculas.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM matriculas")
    registros = cursor.fetchall()
    conexion.close()

    # Agregar datos al cuadro de texto
    if registros:
        cuadro_texto.insert(tk.END, "===== MATRÍCULAS EN LA BASE DE DATOS =====\n")
        for registro in registros:
            cuadro_texto.insert(
                tk.END,
                f"ID: {registro[0]}, Matrícula: {registro[1]}, Año: {registro[2]}, "
                f"Tipo Alumno: {registro[3]}, Carrera: {registro[4]}, Número Alumno: {registro[5]}\n"
            )
    else:
        cuadro_texto.insert(tk.END, "No hay datos en la base de datos.")


#####################3
import tkinter as tk
from tkinter import messagebox

def generar_y_guardar_matricula():
    try:
        tipo_alumno = int(entry_tipo_alumno.get())
        num_carrera = int(entry_carrera.get())
        num_alumno = int(entry_num_alumno.get())

        if tipo_alumno not in [1, 2]:
            raise ValueError("El tipo de alumno debe ser 1 o 2.")
        if num_carrera < 1 or num_carrera > 7:
            raise ValueError("El número de carrera debe estar entre 1 y 7.")
        if num_alumno < 1 or num_alumno >= 1000:
            raise ValueError("El número de alumno debe estar entre 1 y 999.")

        # Generar matrícula
        generador = GeneradorMatricula()
        matricula = generador.generar_matricula(tipo_alumno, num_carrera, num_alumno)

        # Guardar en la base de datos
        guardar_matricula(matricula, generador.anio_actual, tipo_alumno, num_carrera, num_alumno)
        messagebox.showinfo("Matrícula generada", f"La matrícula generada es: {matricula}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Configuración de la interfaz gráfica
def crear_interfaz():
    global entry_tipo_alumno, entry_carrera, entry_num_alumno

    ventana = tk.Tk()
    ventana.title("Generador de Matrículas")
    ventana.geometry("400x300")

    # Etiquetas y entradas
    tk.Label(ventana, text="Tipo de Alumno (1: Transferido, 2: Examen)").pack(pady=5)
    entry_tipo_alumno = tk.Entry(ventana)
    entry_tipo_alumno.pack(pady=5)

    tk.Label(ventana, text="Número de Carrera (1-7)").pack(pady=5)
    entry_carrera = tk.Entry(ventana)
    entry_carrera.pack(pady=5)

    tk.Label(ventana, text="Número de Alumno (1-999)").pack(pady=5)
    entry_num_alumno = tk.Entry(ventana)
    entry_num_alumno.pack(pady=5)

    # Botón para generar matrícula
    tk.Button(ventana, text="Generar Matrícula", command=generar_y_guardar_matricula).pack(pady=20)
    #
    tk.Button(ventana, text="Mostrar Base de Datos", command=mostrar_datos_en_gui).pack(pady=10)


    ventana.mainloop()

# Inicializar base de datos y ejecutar interfaz
if __name__ == "__main__":
    inicializar_base_datos()
    crear_interfaz()