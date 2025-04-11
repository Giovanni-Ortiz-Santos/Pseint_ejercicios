import tkinter as tk
from tkinter import messagebox
import sqlite3
from generador import GeneradorMatricula
from base_datos import guardar_matricula
from sumatoria import Sumatoria
from TiendaAbarrotes import TiendaAbarrotes


# Función para generar una sumatoria
def generar_sumatoria(entry_n_valor_tipo):
    try:
        n_valor_tipo = int(entry_n_valor_tipo.get())
        generador = Sumatoria()
        sumatoria_valor = generador.sumatoria_espo(n_valor_tipo)
        messagebox.showinfo("Resultado", f"Resultado de la sumatoria: {sumatoria_valor}")    
    except ValueError as e:
        messagebox.showerror("Error", str(e))


# Función para generar y guardar una matrícula
def generar_y_guardar_matricula(entry_tipo_alumno, entry_carrera, entry_num_alumno):
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


# Función para mostrar los datos almacenados en la base de datos
def mostrar_datos_en_gui():
    # Crear una nueva ventana para mostrar los datos
    ventana_datos = tk.Toplevel()
    ventana_datos.title("Matrículas almacenadas")
    ventana_datos.geometry("500x400")

    # Cuadro de texto para mostrar los datos
    cuadro_texto = tk.Text(ventana_datos, wrap=tk.WORD)
    cuadro_texto.pack(expand=True, fill=tk.BOTH)

    # Conectar a la base de datos y recuperar los registros
    conexion = sqlite3.connect("matriculas.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM matriculas")
    registros = cursor.fetchall()
    conexion.close()

    # Mostrar los datos en el cuadro de texto
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


# Función para abrir la interfaz del generador de matrículas
def interfaz_generador_matriculas():
    ventana_matriculas = tk.Toplevel()
    ventana_matriculas.title("Generador de Matrículas")
    ventana_matriculas.geometry("400x300")

    # Entradas y etiquetas
    tk.Label(ventana_matriculas, text="Tipo de Alumno (1: Transferido, 2: Examen)").pack(pady=5)
    entry_tipo_alumno = tk.Entry(ventana_matriculas)
    entry_tipo_alumno.pack(pady=5)

    tk.Label(ventana_matriculas, text="Número de Carrera (1-7)").pack(pady=5)
    entry_carrera = tk.Entry(ventana_matriculas)
    entry_carrera.pack(pady=5)

    tk.Label(ventana_matriculas, text="Número de Alumno (1-999)").pack(pady=5)
    entry_num_alumno = tk.Entry(ventana_matriculas)
    entry_num_alumno.pack(pady=5)

    # Botones
    tk.Button(ventana_matriculas, text="Generar Matrícula", command=lambda: generar_y_guardar_matricula(
        entry_tipo_alumno, entry_carrera, entry_num_alumno)).pack(pady=10)
    tk.Button(ventana_matriculas, text="Mostrar Matrículas Almacenadas", command=mostrar_datos_en_gui).pack(pady=10)


# Función para abrir la interfaz de sumatoria
def mostrar_datos_en_gui_sumatoria():
    ventana_sumatoria = tk.Toplevel()
    ventana_sumatoria.title("Sumatoria con exponente mayor")
    ventana_sumatoria.geometry("500x400")

    # Entrada y etiqueta
    tk.Label(ventana_sumatoria, text="Número para la sumatoria").pack(pady=5)
    entry_n_valor_tipo = tk.Entry(ventana_sumatoria)
    entry_n_valor_tipo.pack(pady=5)

    # Botón para calcular la sumatoria
    tk.Button(ventana_sumatoria, text="Calcular Sumatoria", command=lambda: generar_sumatoria(entry_n_valor_tipo)).pack(pady=20)



# Función para abrir la interfaz de cálculo de dinero
def mostrar_datos_en_gui_dinero_gastar():
    ventana_dinero = tk.Toplevel()
    ventana_dinero.title("Dinero a gastar")
    ventana_dinero.geometry("500x400")

    # Mostrar cuadro de texto (ejemplo, puedes implementar lógica adicional aquí)
    cuadro_texto = tk.Text(ventana_dinero, wrap=tk.WORD)
    cuadro_texto.pack(expand=True, fill=tk.BOTH)
    cuadro_texto.insert(tk.END, "Aquí puedes calcular cuánto dinero gastarás en el supermercado.")
    
# Función para abrir la interfaz de la tienda de abarrotes
def mostrar_datos_en_gui_tienda():
    tienda = TiendaAbarrotes(saldo_inicial=300)

    ventana_tienda = tk.Toplevel()
    ventana_tienda.title("Tienda de Abarrotes")
    ventana_tienda.geometry("600x400")

    cuadro_texto = tk.Text(ventana_tienda, wrap=tk.WORD)
    cuadro_texto.pack(expand=True, fill=tk.BOTH)
    cuadro_texto.insert(tk.END, tienda.mostrar_opciones())

    # Entrada para elegir productos
    tk.Label(ventana_tienda, text="Ingresa el número del producto que deseas comprar:").pack(pady=5)
    entry_numero_producto = tk.Entry(ventana_tienda)
    entry_numero_producto.pack(pady=5)

    # Botón para comprar productos
    def comprar_producto():
        try:
            numero_producto = int(entry_numero_producto.get())
            tienda.comprar_producto(numero_producto, ventana_tienda, cuadro_texto)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    tk.Button(ventana_tienda, text="Comprar", command=comprar_producto).pack(pady=10)

    # Botón para finalizar compra
    def finalizar_compra():
        resumen = tienda.finalizar_compra()
        messagebox.showinfo("Compra finalizada", resumen)
        ventana_tienda.destroy()

    tk.Button(ventana_tienda, text="Finalizar compra", command=finalizar_compra).pack(pady=10)

    # Entrada para elegir productos
    tk.Label(ventana_tienda, text="Ingresa el número del producto que deseas comprar:").pack(pady=5)
    entry_numero_producto = tk.Entry(ventana_tienda)
    entry_numero_producto.pack(pady=5)

    # Botón para comprar productos
    tk.Button(ventana_tienda, text="Comprar", command=lambda: tienda.comprar_producto(
        int(entry_numero_producto.get()), ventana_tienda, cuadro_texto)).pack(pady=10)

    # Botón para finalizar compra
    tk.Button(ventana_tienda, text="Finalizar compra", command=lambda: tienda.finalizar_compra(ventana_tienda)).pack(pady=10)



# Configuración de la interfaz principal
def crear_interfaz():
    ventana_principal = tk.Tk()
    ventana_principal.title("Programas")
    ventana_principal.geometry("400x300")

    # Botones para los diferentes programas
    tk.Button(ventana_principal, text="Programa Fórmula Sumatoria", command=mostrar_datos_en_gui_sumatoria).pack(pady=10)
    tk.Button(ventana_principal, text="Programa Dinero a gastar", command=mostrar_datos_en_gui_dinero_gastar).pack(pady=10)
    tk.Button(ventana_principal, text="Programa Tienda de Abarrotes", command=mostrar_datos_en_gui_tienda).pack(pady=10)
    tk.Button(ventana_principal, text="Programa Generador de Matrículas", command=interfaz_generador_matriculas).pack(pady=10)

    ventana_principal.mainloop()



