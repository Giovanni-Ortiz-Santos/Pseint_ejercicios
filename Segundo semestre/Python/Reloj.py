import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

# --- CONFIGURACIÓN INICIAL ---
minute_vector = np.array([0, 1])
hour_vector = np.array([0, 0.6])
second_vector = np.array([0, 1.1])

fig, ax = plt.subplots(figsize=(6,6))
ax.set_aspect('equal')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_xticks([])
ax.set_yticks([])
ax.set_facecolor("#f5f5f5")  # Fondo claro

# Dibujamos el círculo del reloj
clock_face = plt.Circle((0, 0), 1, fill=False, edgecolor='black', linewidth=2)
ax.add_artist(clock_face)

# Agregamos números más visibles al reloj
for i in range(1, 13):
    angle = np.deg2rad(i * 30)
    x, y = 0.85 * np.sin(angle), 0.85 * np.cos(angle)
    ax.text(x, y, str(i), fontsize=14, ha='center', va='center', fontweight='bold', color="black")

# Marcas de minutos
for i in range(60):
    angle = np.deg2rad(i * 6)
    x, y = np.sin(angle), np.cos(angle)
    ax.plot([0.95*x, x], [0.95*y, y], color="gray", linewidth=0.8)

# Inicialización de las líneas (manecillas)
minute_hand, = ax.plot([], [], lw=3, color='blue', label="Minuto")
hour_hand, = ax.plot([], [], lw=5, color='red', label="Hora")
second_hand, = ax.plot([], [], lw=1.5, color='green', label="Segundo")
ax.legend(loc="upper right")

# Función para rotar un vector con una transformación lineal
def rotate_vector(v, angle_rad):
    rotation_matrix = np.array([
        [np.cos(angle_rad), -np.sin(angle_rad)],
        [np.sin(angle_rad),  np.cos(angle_rad)]
    ])
    return rotation_matrix @ v

# Función que actualiza la animación según la hora real
def update(frame):
    now = datetime.now()
    minute_angle = np.deg2rad(now.minute * 6)
    hour_angle = np.deg2rad((now.hour % 12) * 30 + now.minute * 0.5)
    second_angle = np.deg2rad(now.second * 6)

    rotated_minute = rotate_vector(minute_vector, -minute_angle)
    rotated_hour = rotate_vector(hour_vector, -hour_angle)
    rotated_second = rotate_vector(second_vector, -second_angle)

    minute_hand.set_data([0, rotated_minute[0]], [0, rotated_minute[1]])
    hour_hand.set_data([0, rotated_hour[0]], [0, rotated_hour[1]])
    second_hand.set_data([0, rotated_second[0]], [0, rotated_second[1]])

    return minute_hand, hour_hand, second_hand

# Animación en tiempo real
ani = FuncAnimation(fig, update, interval=1000)

plt.title("⏰ Reloj Analógico Mejorado", fontsize=16, fontweight="bold")
plt.show()