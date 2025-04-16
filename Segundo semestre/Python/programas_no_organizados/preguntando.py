acomulador = 0
while True: 
    numero_1 =(input("INGRESA UN NUMERO: O PRECIONA S PARA SALIR DEL PROGRAMA ----> "))
    if(numero_1 == "s"):
        break  #rompe el ciclo
    else:
        acomulador =  acomulador+ int(numero_1)
        
if(acomulador > 0):
    print("El resultado final del acomulador es ---> ", acomulador)
else:
    print("Se pulso 5 para salir")
        
