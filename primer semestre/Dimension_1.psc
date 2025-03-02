Algoritmo Dimension_1
	
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
		Escribir vector[r]
		r = r+ 1
	FinMientras
FinAlgoritmo
