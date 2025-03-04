Algoritmo Matrices
	Definir columnas, renglones, e, m, s, matriz Como Entero
	
	Escribir "Dime la cantidad de columnas de la matriz"
	leer columnas
	Escribir "Dime la cantidad de renglones de la matriz"
	leer renglones
	
	Dimension matriz[renglones,columnas]
	
	e = 1
	Mientras e <= renglones Hacer
		m = 1
		Mientras m <= columnas Hacer
			Imprimir "Ingresa la celda ----> [", e,"] [", m,"]"
			Leer matriz[e,m]
			m = m+1
		FinMientras
		e = e+1
	FinMientras
	
	s = 1
	Mientras s <= renglones Hacer
		n = 1
		Mientras n <= columnas
			Escribir Sin Saltar matriz[s,n], " / "
			n = n+1
		FinMientras
		s = s+1
		Imprimir ""
	FinMientras
FinAlgoritmo
