Algoritmo OpcionesMenu
	
	Escribir "Seleccione una de las opciones: "
	Escribir "1. Sumar"
	Escribir "2. Restar"
	Escribir "3. Salir"
	Leer opcionIntroducida
	
	exprecion_logica = opcionIntroducida  == 1 | opcionIntroducida == 2 | opcionIntroducida == 3
	
	Imprimir "La seleccion ", opcionIntroducida, " es una opcion valida?: ", exprecion_logica
	
FinAlgoritmo
