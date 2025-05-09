import tkinter as Tk
from tkinter import messagebox

app=Tk.Tk()
app.title("TECNOLOGICO DE ESTUDIOS SUPERIORES DE JILOTEPEC")
app.configure(bg="yellow")

def saludar():
    messagebox.askquestion("Informacion","Programando en python")

button3 = Tk.Button(text="clik here", command=saludar)
button3.pack()



app.geometry("500x500")
app.mainloop()

"""
Tipos difernete de mensajes
showwarning
showerror
askquestions
askcancel
askyesno
askesnocancel
"""