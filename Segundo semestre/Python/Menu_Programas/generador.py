import time

class GeneradorMatricula:
    def __init__(self):
        self.anio_actual = time.localtime().tm_year  # Obtiene el año actual automáticamente

    def generar_matricula(self, tipo_alumno, num_carrera, num_alumno):
        # Formatear número de alumno con ceros a la izquierda (3 dígitos)
        num_alumno_formateado = f"{num_alumno:03d}"
        return f"{self.anio_actual}{tipo_alumno}{num_carrera}{num_alumno_formateado}"