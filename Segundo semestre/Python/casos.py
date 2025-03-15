a = int(input("Ingresa el primer numero ---> "))
b = int(input("Ingresa el segundo numero ---> "))

print("*** MENU PRINCIPAL ***")
print("{+} suma a+b")
print("{-} resta a-b")
print("{*} multiplicacion a*b")
print("{/} divicion a/b")

simbolo =  input("Ingresa la operacion insertando el simbolo ---> ")
match simbolo: 
    case "+":
        print(f"Resultado es ---> {a+b}")
    case "-":
        print(f"Resultado es ---> {a-b}")
    case "*":
        print(f"Resultado es ---> {a*b}")
    case "/":
        if b !=0:
            print(f"Resultado es ---> {a/b}")
        else: 
            print("no se puede dividir entre 0")
    case _:
        print("Operacion Invalida")