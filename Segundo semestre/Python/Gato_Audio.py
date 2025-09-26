import tkinter as tk
import gtts
import pygame

pygame.mixer.init()
turno = "Jugador 1"
marcas = {"Jugador 1": "X", "Jugador 2": "O"}
tablero = [["" for _ in range(3)] for _ in range(3)]

ventana = tk.Tk()
ventana.title("Juego de Gato")
ventana.geometry("300x350")

def anunciar_ganador(jugador):
    
    mensaje = f"¡Felicidades! {jugador} ha ganado!"
    tts = gtts.gTTS(mensaje, lang="es")
    archivo_audio = "ganador.mp3"
    tts.save(archivo_audio)
    pygame.mixer.music.load(archivo_audio)
    pygame.mixer.music.play()
    
    lbl_estado.config(text=mensaje)

def verificar_ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != "":
            jugador_ganador = "Jugador 1" if tablero[i][0] == "X" else "Jugador 2"
            anunciar_ganador(jugador_ganador)
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != "":
            jugador_ganador = "Jugador 1" if tablero[0][i] == "X" else "Jugador 2"
            anunciar_ganador(jugador_ganador)
            return True
    
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != "":
        jugador_ganador = "Jugador 1" if tablero[0][0] == "X" else "Jugador 2"
        anunciar_ganador(jugador_ganador)
        return True
    
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != "":
        jugador_ganador = "Jugador 1" if tablero[0][2] == "X" else "Jugador 2"
        anunciar_ganador(jugador_ganador)
        return True

    if all(tablero[i][j] != "" for i in range(3) for j in range(3)):
        lbl_estado.config(text="¡Empate!")
        tts = gtts.gTTS("¡El juego terminó en empate!", lang="es")
        tts.save("empate.mp3")
        pygame.mixer.music.load("empate.mp3")
        pygame.mixer.music.play()
        return True

    return False

def presionar_boton(row, col, boton):
    global turno
    if tablero[row][col] == "":
        tablero[row][col] = marcas[turno]
        boton.config(text=marcas[turno])

        if not verificar_ganador():
            turno = "Jugador 2" if turno == "Jugador 1" else "Jugador 1"
            lbl_estado.config(text=f"Turno de {turno}")

botones = []
for i in range(3):
    fila = []
    for j in range(3):
        btn = tk.Button(ventana, text="", font=("Arial", 20), width=5, height=2,
                        command=lambda x=i, y=j, b=None: presionar_boton(x, y, b))
        btn.grid(row=i, column=j, padx=5, pady=5)
        fila.append(btn)
    botones.append(fila)

for i in range(3):
    for j in range(3):
        botones[i][j].config(command=lambda x=i, y=j, b=botones[i][j]: presionar_boton(x, y, b))

lbl_estado = tk.Label(ventana, text="Turno de Jugador 1", font=("Arial", 12))
lbl_estado.grid(row=3, column=0, columnspan=3, pady=10)

ventana.mainloop()