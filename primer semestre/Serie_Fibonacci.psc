Algoritmo sin_titulo
	Definir x, c, a, b, cont  Como Entero

	Imprimir  'digite el final de la serie fibonasi'
	Leer x
	a = 0 
	b = 1
	c = 0
	cont = 0
	
	Mientras  cont <= x Hacer
		imprimir cont ,' / ', c 
		a = b
		b = c
		c = a + b
		cont = cont + 1
	FinMientras
FinAlgoritmo