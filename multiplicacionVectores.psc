Algoritmo multiplicacionVectores
	//Pedir datos
	validacion = Falso
	Mientras validacion == Falso Hacer
		Escribir "Escribe la cantidad de filas de la primera matriz"
		Leer filas_1
		Escribir "Escribe la cantidad de columnas de la primera matriz"
		Leer columnas_1
		
		Escribir "Escribe la cantidad de filas de la segunda matriz"
		Leer filas_2
		Escribir "Escribe la cantidad de columnas de la segunda matriz"
		leer columnas_2
		
		si filas_1 == filas_2 Entonces
			validacion_1 = Verdadero
		FinSi
		
		si columnas_1 == columnas_2 Entonces
			validacion_2 = Verdadero
		FinSi
		
		si validacion_1 y validacion_2 Entonces
			validacion = Verdadero
		FinSi
		Imprimir "El tamaño de matrices no es valido"
		Imprimir "Verifique que sean iguales dimenciones (filas y columnas)"
		Escribir ""
	FinMientras
	
	
	// Declarar variables
	Dimension matriz_1[filas_1,columnas_1]
	Dimension matriz_2[filas_2,columnas_2]
	Dimension multiplicacion[filas_2,columnas_2]
	
	//Ingreso de datos para la primera matriz
	filaContador = 1
	Imprimir "Ingresa valores para la primera matriz."
	Mientras filaContador <= filas_1 Hacer
		columnaContador = 1
		Mientras columnaContador <= columnas_1 Hacer
			Imprimir "Ingresa la celda ----> [", filaContador,"] [", columnaContador,"]"
			Leer matriz_1[filaContador,columnaContador]
			columnaContador = columnaContador+1
		FinMientras
		filaContador = filaContador+1
	FinMientras
	
	//Ingreso de datos para la segunda matriz
	Imprimir "Ingrese valores para la segunda matriz"
	filaContador = 1
	Mientras filaContador <= filas_2 Hacer
		columnaContador = 1
		Mientras columnaContador <= columnas_2 Hacer
			Imprimir "Ingresa la celda ----> [", filaContador,"] [", columnaContador,"]"
			Leer matriz_2[filaContador,columnaContador]
			columnaContador = columnaContador+1
		FinMientras
		filaContador = filaContador+1
	FinMientras
	
	//Multiplicacion de matrices
	filaContador = 1
	Mientras filaContador <= filas_2 Hacer
		columnaContador = 1
		Mientras columnaContador <= columnas_2 Hacer	
			multiplicacion[filaContador,columnaContador]= matriz_1[filaContador,columnaContador]*matriz_2[filaContador,columnaContador]
			columnaContador = columnaContador+1
		FinMientras
		filaContador = filaContador+1
	FinMientras
	
	//Imprecion de matrices 1
	filaContador = 1
	Mientras filaContador <= filas_1 Hacer
		columnaContador = 1
		Mientras columnaContador <= columnas_1 Hacer	
			Imprimir Sin Saltar matriz_1[filaContador, columnaContador], " | "			
			columnaContador = columnaContador+1
		FinMientras
		Imprimir sin saltar"    "
		
		columnaContador = 1
		Mientras columnaContador <= columnas_2 Hacer	
			Imprimir Sin Saltar matriz_2[filaContador, columnaContador], "	 | "		
			columnaContador = columnaContador+1
		FinMientras
		Imprimir sin saltar"    "
		
		//Imprecion de multiplicacion
		columnaContador = 1
		Mientras columnaContador <= columnas_2 Hacer	
			Imprimir Sin Saltar multiplicacion[filaContador, columnaContador], " | "	
			columnaContador = columnaContador+1
		FinMientras
		Imprimir ""
		filaContador = filaContador+1
		
	FinMientras
FinAlgoritmo
