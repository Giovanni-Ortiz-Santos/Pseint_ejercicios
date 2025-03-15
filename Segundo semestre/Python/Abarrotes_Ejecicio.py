"""Realizar un programa que solicite la cantidad a gastar en una tienda de barrotes.
Intrucciones:
    El programa debe finalizar cuando ya no tenga saldo disponible.
    El programa debe solicitar que producto se va adquieriendo y el costo de cada uno.
    Si tengo saldo disponible y quiero un producto mayor al saldo no me lo debe vender, 
    me debe insistir mi saldo disponible 
"""

print("*** TIENDA DE ABARROTES ***")    
mi_saldo = 300
acomulador = 0

productos =["Papa", "Chile", "Jitomate", "Cebolla", "Brocoli", "Tortillas","Vino Tinto", "Cerveza", "Celular del oxxo","Mango"]
precios_productos = [20.0, 15.0,40.0,30.0,25.0,23.0,150.0,57.0,1999.9,50.0]

opciones = """
Productos a comprar ():
\t1-Papa -------------- 20.0
\t2-Chile ------------- 15.0
\t3-Jitomate  --------- 40.0
\t4-Cebolla ----------- 30.0
\t5-Brocoli ----------- 25.0
\t6-Tortillas --------- 23.0
\t7-Vino Tinto -------- 150.0
\t8-Cerveza ----------- 57.0 
\t9-Celular del oxxo -- 1999.9
\t10-Mango ------------- 50.0
"""

print(opciones)

while True: 
    numero_ingresado =int(input("INGRESA UN NUMERO SEGUN EL PRODUCTO QUE NESESITES ----> "))
    acomulador =  acomulador+ precios_productos[(numero_ingresado-1)]
    
    
    if (precios_productos[(numero_ingresado-1)] >mi_saldo):
        acomulador = acomulador - precios_productos[(numero_ingresado-1)]
        print("No se puede comprar el producto. Saldo insuficiente.")
        
        
    if(acomulador >mi_saldo):
        print("Te falta saldo para el produtcto, cambia a otro o selecciona \"s\" para salir del programa")
        acomulador = acomulador - precios_productos[(numero_ingresado-1)]
        
    print("Estado de la compra ----> Producto: ",productos[(numero_ingresado-1)],"  Precio: ", 
        precios_productos[(numero_ingresado-1)],"   Costo del carrito: ",acomulador) 
        
    if(acomulador >= mi_saldo):
        
        break  #rompe el ciclo

if(acomulador > 0):
    print("El resultado final de la compra es ---> ", acomulador)

        
