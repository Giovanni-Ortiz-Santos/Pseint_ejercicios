
	Algoritmo SumaDeVectores
		
		Escribir "Ingresa la longitud del vector: "
		leer longitud_vector
		serieDeSuma = 0
		inicializacion = 1
		Dimension vector[longitud_vector]
		Mientras inicializacion <= longitud_vector Hacer
			Imprimir "Ingrese un numero para la posicion ----> [", inicializacion, "] = "		
			leer vector[inicializacion]
			serieDeSuma = serieDeSuma + vector[inicializacion]
			inicializacion = inicializacion + 1		
			
			
		FinMientras
		
		imprimir "Pulsa enter para continuar "
		leer z
		
		Imprimir "Se imprimen los valores del vector"
		r = 1
		
		Mientras r <= longitud_vector Hacer
			Escribir  Sin Saltar vector[r], " / "
			r = r+ 1
		FinMientras
		
		Imprimir ""
		Imprimir "La suma de los vectores es de: "	serieDeSuma	
FinAlgoritmo


