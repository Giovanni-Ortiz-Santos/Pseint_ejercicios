n1 = int(input("Ingresa tu calificacion -----> "))
if n1==100:
    print("Excelente calificacion")
elif n1 <=99 and n1>=90:
    print("MUY BIEN")
elif n1<=89 and n1 >=80:
    print("BIEN")
elif n1 <= 79 and n1>= 70:
    print("Alumno Regular")
else:
    print("REPROBADO")