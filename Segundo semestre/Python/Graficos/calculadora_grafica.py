import tkinter as tk

def click_button(valor):
    entry.insert(tk.END, valor)

def calcular():
    try:
        resultado = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, resultado)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def borrar():
    entry.delete(0, tk.END)

ventana = tk.Tk()
ventana.config(bg="yellow")
ventana.title("Calculadora")

entry = tk.Entry(ventana, width=40, font=('Arial', 14), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('**',5,0)

]

for texto, fila, columna in botones:
    if texto == '=':
        boton = tk.Button(ventana, text=texto, width=10, height=5, command=calcular)
    else:
        boton = tk.Button(ventana, text=texto, width=10, height=5,  command=lambda t=texto: click_button(t))
    boton.grid(row=fila, column=columna)

boton_borrar = tk.Button(ventana, text="C", width=10, height=5, command=borrar)
boton_borrar.grid(row=5, column=0, columnspan=4)

ventana.mainloop()
