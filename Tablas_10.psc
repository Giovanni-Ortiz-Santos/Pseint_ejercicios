Algoritmo Tablas_10
	
	Definir a, b, r, z Como Entero
	
	a = 1
	
	Mientras a <= 10 Hacer
		b = 1
		Mientras  b <= 10
			r = b * a
			Imprimir a, ' * ' , b, " = " r
			b = b + 1
		FinMientras
		
		Imprimir  "Pulsa enter por contador "
		Leer z
		Borrar Pantalla
		a = a + 1
	FinMientras
	
FinAlgoritmo
