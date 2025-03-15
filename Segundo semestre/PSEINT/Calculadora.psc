Funcion suma(n1, n2)
	x = n1 + n2 
	escribir "El resultado es ", x
FinFuncion

Funcion resta(n1, n2)
	x = n1 - n2 
	escribir "El resultado es ", x
FinFuncion

Funcion multiplicacion(n1, n2)
	x = n1 * n2 
	escribir "El resultado es ", x
FinFuncion

Funcion division(n1, n2)
	x = n1 / n2 
	escribir "El resultado es ", x
FinFuncion

Funcion residuo(n1, n2)
	x = n1 % n2 
	escribir "El resultado es ", x
FinFuncion

Algoritmo Calculadora
	
	Escribir "Dame un numero "
	leer n1
	Escribir "Dame otro numero "
	leer n2
	
	Imprimir "*** Menu de operaciones ***"
	Imprimir "Seleccione con un numero la operacion que desee"
	Imprimir "1: Suma de 2 numeros"
	Imprimir "2: Resta de 2 numeros"	
	Imprimir "3: Multiplicacion de 2 numeros"
	Imprimir "4: División de 2 numeros"
	Imprimir "5: Residuo de 2 numeros"
	Imprimir "Elije una opcion"
	Leer opc	
	Segun opc Hacer
		1: 
			suma(n1,n2)
		2:
			resta(n1,n2)
		3:
			multiplicacion(n1,n2)
		4:
			division(n1,n2)
		5:
			residuo(n1,n2)
		De Otro Modo:
			Imprimir "Opcion incorrecta. Ingrese una opcion valida"
			
	FinSegun
	
FinAlgoritmo
