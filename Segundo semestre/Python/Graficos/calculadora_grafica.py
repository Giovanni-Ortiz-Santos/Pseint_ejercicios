import tkinter as tk
from tkinter import messagebox

ventanaCalculadora = tk.Tk()
ventanaCalculadora.title("Calculadora ISIC")
ventanaCalculadora.configure(bg="blue")
ventanaCalculadora.geometry("600x600")

labelEntry = tk.Label(width=30, height=3, text="0",anchor="e", font=("Arial",20,"bold")).pack(pady=50)
boton1 = tk.Button(text="1", font=("Arial", 14,"bold"), width=5, height=2).pack(side="left",padx=10)
boton2 = tk.Button(text="2", font=("Arial", 14,"bold"), width=5, height=2).pack(side="left",padx=10)
boton3 = tk.Button(text="3", font=("Arial", 14,"bold"), width=5, height=2).pack(side="left",padx=10)
boton4 = tk.Button(text="4", font=("Arial", 14,"bold"), width=5, height=2).pack(side="left",padx=10)



ventanaCalculadora.mainloop()