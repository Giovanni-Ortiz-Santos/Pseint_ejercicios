Algoritmo Ordenamiento_de_Numeros
	
	Definir n1, n2, n3 Como Entero
	
	Imprimir "Ingrese un primer valor: "
	Leer n1
	
	Imprimir "Ingrese un segundo valor: "
	leer n2
	
	Imprimir "Ingrese un terecer valor: "
	Leer n3
	
	Si n1 == n2 Entonces
		
		si n2 == n3 Entonces
			Imprimir n1, "/ ", n2, "/ ", n3
		SiNo
			si n1 > n3 Entonces
				Imprimir n1, "/ ", n2 ,"/ ", n3
			SiNo
				Imprimir n3,'/ ',n1,'/ ',n2
			FinSi
		FinSi
		
	SiNo
		si n1 > n2 Entonces
			si n1 > n3 Entonces
				si n2 > n3 Entonces
					Imprimir n1, '/ ',  n2, '/ ',  n3
				SiNo
					Imprimir n1,'/ ',  n3, '/ ',  n2
				FinSi
			SiNo
				Imprimir n3, '/ ', n1, '/ ', n2
			FinSi
		SiNo
			si n2 > n3 Entonces
				si n1 > n3 Entonces
					Imprimir n2, '/ ', n1, '/ ', n3
				SiNo
					Imprimir n2, '/ ',  n3, '/ ', n1
				FinSi
			SiNo
				Imprimir n3, '/ ',  n2,'/ ', n1
			FinSi
		FinSi
		
	FinSi
	
FinAlgoritmo
