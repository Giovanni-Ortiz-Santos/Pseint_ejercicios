print("Bienvenido a la Calculadora.")
operacion = int(input("""
Operaciones Disponibles, selecciona una opcion
    1 Suma
    2 Resta
    3 Multiplicacion 
    4 Divicion
Elija su Opcion: """))

if operacion:
    num1= float(input("Ingresa el primer numero: "))
    num2= float(input("Ingresa el segundo numero: "))

def suma():
    op_suma = num1 + num2 
    print(op_suma)

def resta():
    op_resta = num1 - num2 
    print(op_resta)

def multiplicacion():
    op_multiplicacion = num1 * num2 
    print(op_multiplicacion)

def divicion():
    if num1 == 0 or num2 == 0:
        print("Error divicion por cero")
    else:
        op_divicion = num1 / num2   
        print(op_divicion)

match (operacion):
    case 1:
        suma() 
    case 2:
        resta()
    case 3:
        multiplicacion()
    case 4:
        divicion()

