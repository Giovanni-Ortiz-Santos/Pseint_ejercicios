# Importacion de los paquetes
import time 

# Arreglo para las matriculas y variables
matriculas=[]

# Libreria time
hora_actual = time.strftime("%Y")


#Ingreso de matriculas
n = int(input("Cuantos ID deseas generar ---> "))

#Evalucion, itercion y creacion de matriculas 
for i in range(n):
    
    # Evalucion de los datos 
    print(F"ID. numero: {i+1}")
    periodo = int(input("Ingresa el tipo de periodo (2 ó 1) ---> "))
    carrera = int(input("Ingresa el numero de la carrera ---> "))
    num_alumno = int(input("Ingresa el numero de ingreso de alumno ---> "))
    
    if num_alumno < 1000:
        print("Id: ",hora_actual,periodo,carrera,num_alumno)    
    else:
        print("No es posible generar el id, Numeros incorrecto introducidos")
            
    
    
    
    
