import time

#variables
hay_valores = True
whilo_validacion = True
incremento_compra = 0
iva_aumento = 16

#arreglos
lista_productos=[]
lista_precios = []
descripcion_producto = []

#Diccionario
diccionario = {"producto":lista_productos, 
            "precio_unitario":lista_precios, 
            "descripcion_prod":descripcion_producto}

#ingreso de los datos (nombre_empresa, direccion, fecha)
nombre_empresa = input("Ingresa el nombre de la empresa: ")
direccion_empresa = input("Ingresa la direcion de la empresa: ")
fecha_actual = time.strftime("%d/%m/%Y")



# Ingreso de los productos
while whilo_validacion:
    validar =input("Deseas comprar un producto (\"si\"/\"no\"): ").lower()
    if (validar == "si"):
            ingreso_productos = input("Nombre del Producto: ")
            lista_productos.append(ingreso_productos)    
            ingreso_precios = int(input("Precio Unitario del producto: "))
            lista_precios.append(ingreso_precios)
            ingreso_descripcion = input("Descripcion del producto: ")
            descripcion_producto.append(ingreso_descripcion)
            whilo_validacion = True
            
            #incremento
            incremento_compra = ingreso_precios + incremento_compra
            hay_valores = True
    elif(validar == "no"):
        whilo_validacion = False
        
        if(incremento_compra > 0):
            hay_valores =  True
        else:
            hay_valores = False
        
    else:
        print("Ingrese una opcion valida.")
        whilo_validacion = True
    

if(hay_valores):
    #operaciones    
    iva_total = (incremento_compra * iva_aumento)/100        
    total_pagar = incremento_compra + iva_total
    print()

    print(f"""---------------------------------
NOTA DE REMISIÓN.
    Nombre de la empresa: {nombre_empresa}
    Direccion: {direccion_empresa}
    Fecha: {fecha_actual}
    Producto             Precio unitario
""")
    # Iterar sobre cada producto e imprimirlo
    for prod, precio in zip(diccionario["producto"], diccionario["precio_unitario"]):
        print(f"     {prod:<20}{precio:>10.2f}")

    print(f"""
Total: {incremento_compra}
    Iva: {iva_total} 
    Total a pagar: {total_pagar}
""")
else:
    print("Gracias por su preferencia. Buen dia. :)")