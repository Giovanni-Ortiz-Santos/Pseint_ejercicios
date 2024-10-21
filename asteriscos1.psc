Algoritmo asteriscos1
	
	Definir colv, filh, cont Como Entero
	Imprimir "Ingrese el total de asteriscos"
	Leer colv 
	cont = 1
	Mientras cont <= colv Hacer
		filh = 1
		Mientras  filh <= colv
			si cont =  1 o cont = colv o filh = 1 o filh = colv Entonces
				Imprimir Sin Saltar "*"
			SiNo
				Imprimir Sin Saltar " "
			FinSi
			filh =  filh + 1
		FinMientras
		Imprimir ""
		cont = cont + 1
	FinMientras
	
FinAlgoritmo
