Algoritmo CalculoTerreno
	Escribir "Programa para calcular el precio de un terreno."
	
	Escribir "Escriba el ancho del terreno (metros: )"
	leer ancho
	
	Escribir "Escriba el lago del terreno(metros): "
	leer largo
	
	Escribir "Escriba el precio por metro cuadrado: "
	leer precio_m2
	
	area  = ancho * largo
	precio_total = area * precio_m2
	
	Imprimir "Area del terreno: ", area
	Imprimir "Precio del terreno: ", precio_total
	
FinAlgoritmo
