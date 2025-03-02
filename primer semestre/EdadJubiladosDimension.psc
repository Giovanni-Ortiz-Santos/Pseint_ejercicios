
	// 1.- Hacer un algoritmo que solcite la diencion de un vector
	// 2.- Dicho vector almacenara edades de los trabajadores
	// 3.- El Algoritmo debe visualizar unicamente aquellas edades mayores o iguales a 60 años que se van a jubilar 
	
	
	Algoritmo EdadJubiladosDimension
		
		Escribir "Ingresa la longitud del vector: "
		leer longitud_vector		
		inicializacion = 1
		Dimension vector[longitud_vector]
		Mientras inicializacion <= longitud_vector Hacer
			Imprimir "Ingrese un numero para la posicion ----> [", inicializacion, "] = "		
			leer vector[inicializacion]
			
			inicializacion = inicializacion + 1							
		FinMientras		
		imprimir "Pulsa enter para continuar "
		leer z		
		Imprimir "Se imprimen los valores del vector"
		r = 1		
		Mientras r <= longitud_vector Hacer
			si vector[r] >= 60 Entonces
				Imprimir "Edad del jubilado: ", vector[r]
			FinSi
			r = r+ 1
		FinMientras

FinAlgoritmo




