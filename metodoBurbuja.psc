Algoritmo metodoBurbuja
	Escribir "Dame la longitud del vector" //Mensaje de los datos ingresados
	leer x //Lectura de los datos 
	
	Dimension v[x] // Declaramos el vector 
	
	// Inicio de un ciclo para pedir los numeros a ingresar
	d = 1 // Variable de inicializacion
	Mientras d <=x Hacer
		Escribir  "Ingresa un numero para la posicion ------> [", d, "] = " //Ingreso de numeros
		Leer v[d] // Lectura y almacenamiento al vector
		d = d+1 // Variable de incremento 
	FinMientras
	
	// Ciclo para realizar el metodo de acomodo de vectores ()
	a = 1 // Variable de inicializacion
	aux = 0 // Declaracion de variable para su uso despues 
	Mientras a <= x Hacer
		b = 1
		Mientras b <=x -1 Hacer
			si v[b] < v[b+1] Entonces
				aux = v[b];				
				v[b] = v [b+1]
				v[b+1] = aux;
			FinSi
			b = b+1
		FinMientras
		a =a+1
	FinMientras
	r = 1
	mientras r <= x Hacer
		Escribir v[r]
		r=r+1
	FinMientras
FinAlgoritmo
