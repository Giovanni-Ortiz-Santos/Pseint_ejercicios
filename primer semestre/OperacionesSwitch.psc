Algoritmo sin_titulo
	Imprimir "Captura un numero: "
	leer x
	Imprimir "Captura otro numero: "
	leer r
	Borrar Pantalla
	Imprimir "Menu principal."
	Imprimir "1: suma"
	Imprimir "2: resta"
	Imprimir "3: multiplicacion"
	Imprimir "Elija una opcion"
	Leer z
	
	Imprimir "Tus numeros selecionados son ", x, " y ", r 
	segun z Hacer
		1:
			a = x + r
			Imprimir "El resultado de la operacion suma es ---> ", a
		2:
			a = x - r
			Imprimir "El resultado de la operacion resta es ---> ", a
		3:
			a = x * r
			Imprimir "El resultado de la operacion multiplcacion es ---> ", a
		De Otro Modo:
			Imprimir "No existe una operacion con ese numero, ejecute nuevamente el programa"
	FinSegun
FinAlgoritmo
