class Sumatoria:
    def sumatoria_espo(self,n_valor_tipo):
        a = 1        
        sumatoria = 0
        while a <= n_valor_tipo:
            n_valor_exponente = a**(a+1)
            print(f"{a}^{(a+1)} = {n_valor_exponente}")
            sumatoria = n_valor_exponente + sumatoria
            a = a +1
        return sumatoria
    







#--------------------------------------------------------------------------#




import tkinter as tk


def mostrar_datos_en_gui_sumatoria():
    
    global entry_n_valor_tipo
    ventana_datos = tk.Toplevel()
    ventana_datos.title("Sumatoria con exponente mayor")
    ventana_datos.geometry("500x400")

    
    tk.Label(ventana_datos, text="Número de Alumno (1-999)").pack(pady=5)
    entry_n_valor_tipo = tk.Entry(ventana_datos)
    entry_n_valor_tipo.pack(pady=5)
    tk.Button(ventana_datos, text="Generar Matrícula", command=lambda: generar_sumatoria(entry_n_valor_tipo)).pack(pady=20)                            
    
    
######################################################################

def mostrar_datos_en_gui_Dinero_Gastar():
    ventana_datos = tk.Toplevel()
    ventana_datos.title("DINERO A GASTAR EN EL SUPERMERCADO")
    ventana_datos.geometry("500x400")

    # Cuadro de texto para mostrar los datos
    cuadro_texto = tk.Text(ventana_datos, wrap=tk.WORD)
    cuadro_texto.pack(expand=True, fill=tk.BOTH) 
    
######################################################################

def mostrar_datos_en_gui_Matricula():
    ventana_datos = tk.Toplevel()
    ventana_datos.title("MATRICULAS ALMACENADAS")
    ventana_datos.geometry("500x400")

    # Cuadro de texto para mostrar los datos
    cuadro_texto = tk.Text(ventana_datos, wrap=tk.WORD)
    cuadro_texto.pack(expand=True, fill=tk.BOTH)    
    
#######################################################################

import tkinter as tk
from tkinter import messagebox


def generar_sumatoria(entry_n_valor_tipo):
    try:
        n_valor_tipo = int(entry_n_valor_tipo.get())
        
        # Generar Sumatoria
        generador = Sumatoria()
        sumatoria_valor = generador.sumatoria_espo(n_valor_tipo)
        messagebox.showinfo("Matrícula generada", f"La matrícula generada es: {sumatoria_valor}")    
    
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    

##################################################

# Configuración de la interfaz gráfica
def crear_interfaz():
    

    ventana = tk.Tk()
    ventana.title("Generador de Matrículas")
    ventana.geometry("400x300")

    # Etiquetas y entradas(botones para los programas)
    tk.Button(ventana, text="Programa Formula Sumatoria", command=mostrar_datos_en_gui_sumatoria).pack(pady=10)
    
    tk.Button(ventana, text = "Programa Dinero a gastar",command=mostrar_datos_en_gui_Dinero_Gastar).pack(pady =10)

    tk.Button(ventana, text = "Programa GeneradorMatricula",command=mostrar_datos_en_gui_Matricula).pack(pady=10)
    



    


    ventana.mainloop()

# Inicializar base de datos y ejecutar interfaz
if __name__ == "__main__":
    
    crear_interfaz()