import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # Para gráficas 3D

# --- GRÁFICA PARA EJERCICIO 3: Vectores r1, r2 y su Producto Cruz en 3D ---
print("Generando gráfica para el Ejercicio 3...")

# Definimos los vectores en t=1 (como calculamos antes)
# Vector A (r1(1))
A = np.array([1, 1, 1])
# Vector B (r2(1))
B = np.array([-1, 1, 2])
# Vector C (r1(1) x r2(1))
C = np.array([1, -3, 2])

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Origen de los vectores
origin = [0, 0, 0]

# Dibujar el vector A
ax.quiver(*origin, *A, color='r', label=r'$\vec{r_1}(1)$')
# Dibujar el vector B
ax.quiver(*origin, *B, color='g', label=r'$\vec{r_2}(1)$')
# Dibujar el vector C (producto cruz)
ax.quiver(*origin, *C, color='b', label=r'$\vec{r_1}(1) \times \vec{r_2}(1)$')

# Etiquetas y Título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Ejercicio 3: Vectores r1, r2 y su Producto Cruz en t=1')
ax.legend()

# Establecer límites para una mejor visualización (ajustar si es necesario)
max_val = max(np.max(np.abs(A)), np.max(np.abs(B)), np.max(np.abs(C))) + 1
ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])
ax.set_zlim([-max_val, max_val])

ax.grid(True)
plt.show()

# --- GRÁFICA PARA EJERCICIO 4: Trayectoria, Velocidad y Aceleración en 2D ---
print("\nGenerando gráfica para el Ejercicio 4...")

# a) Grafica la trayectoria: y = 1 - x^3
x_vals = np.linspace(-2, 2, 400) # Rango de t (que es x)
y_vals = 1 - x_vals**3

plt.figure(figsize=(10, 8))
plt.plot(x_vals, y_vals, label='Trayectoria: $y = 1 - x^3$', color='purple')

# b) Dibujar los vectores de velocidad y aceleración en t=1 (x=1)
# En t=1:
# r(1) = (1, 1 - 1^3) = (1, 0) -> Punto de aplicación de los vectores
# v(1) = (1, -3)
# a(1) = (0, -6)

# Punto de aplicación de los vectores (r(1))
point_of_application = np.array([1, 0])

# Vector Velocidad v(1)
plt.quiver(point_of_application[0], point_of_application[1], 1, -3,
           color='red', scale=10, scale_units='xy', angles='xy',
           label='Vector Velocidad $v(1)$')

# Vector Aceleración a(1)
plt.quiver(point_of_application[0], point_of_application[1], 0, -6,
           color='blue', scale=10, scale_units='xy', angles='xy',
           label='Vector Aceleración $a(1)$')

# Marcar el punto de aplicación
plt.plot(point_of_application[0], point_of_application[1], 'ko', markersize=5, label='Punto en $t=1$')


# Etiquetas y Título
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Ejercicio 4: Trayectoria y Vectores de Velocidad/Aceleración en t=1')
plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
plt.axvline(0, color='gray', linestyle='--', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.axis('equal') # Para que las unidades sean del mismo tamaño en ambos ejes
plt.xlim([-2.5, 2.5]) # Ajustar límites si es necesario
plt.ylim([-8, 2])    # Ajustar límites si es necesario
plt.show()