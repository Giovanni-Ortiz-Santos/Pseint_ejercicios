import tkinter as Tk #alias Tk

def suma():
    num1=int(entry_num1.get()) #entry_num1 es la caja de texto 1
    num2=int(entry_num2.get()) #entry_num2 es la caja de texto 1
    resultado=num1+num2
    label_resultado.config(text="resultado " + str(resultado)) #asigna el
    
def resta():
    num1=int(entry_num1.get()) #entry_num1 es la caja de texto 1
    num2=int(entry_num2.get()) #entry_num2 es la caja de texto 1
    resultado=num1-num2
    label_resultado.config(text="resultado " + str(resultado)) #asigna el

def multiplicacion():
    num1=int(entry_num1.get()) #entry_num1 es la caja de texto 1
    num2=int(entry_num2.get()) #entry_num2 es la caja de texto 1
    resultado=num1*num2
    label_resultado.config(text="resultado " + str(resultado)) #asigna el

def division():
    num1=int(entry_num1.get()) #entry_num1 es la caja de texto 1
    num2=int(entry_num2.get()) #entry_num2 es la caja de texto 1
    resultado=num1/num2
    label_resultado.config(text="resultado " + str(resultado)) #asigna el
    
app = Tk.Tk() #ventana o formulario= app el alias Tk
app.title("TECNOLOGICO DE ESTUDIOS SUPERIORES DE JILOTEPEC")

label_num1=Tk.Label(text="primer numero") #label_num1 es de tipo label
entry_num1=Tk.Entry() # capturar el primer valor

label_num2=Tk.Label(text="segundo numero")#label_num2 es de tipo label
entry_num2=Tk.Entry() #capturar el segundo valor

label_resultado = Tk.Label(text=" *****") #label resultado es de tipo
button_suma= Tk.Button(text="sumar", command=suma) #boton_suma es de tipo 
button_resta= Tk.Button(text="resta", command=resta) #boton_suma es de tipo 
button_multiplicacion= Tk.Button(text="multiplicacion", command=multiplicacion) #boton_suma es de tipo 
button_diviion= Tk.Button(text="division", command=division) #boton_suma es de tipo 

label_num1.pack() #empaquetar y mostrar label_num1 en pantalla
entry_num1.pack() #empaquetar y mostrar la caja de texto entry_num1 en pantalla

label_num2.pack()
entry_num2.pack()

label_resultado.pack()
button_suma.pack(pady=5)
button_resta.pack(pady=5)
button_multiplicacion.pack(pady=5)
button_diviion.pack(pady=5)

app.geometry("500x500")
app.mainloop()
