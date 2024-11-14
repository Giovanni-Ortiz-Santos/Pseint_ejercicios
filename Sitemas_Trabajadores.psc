Algoritmo Sitemas_Trabajadores
	Definir nombre_del_trabajador, direccion, puesto Como Caracter
	Definir sueldo_semanal, dias_trabajados, horas_extras_trabajadas Como Real		
	
	Escribir "Sueldo semanal: "
	leer sueldo_semanal
	
	Escribir "Dias trabajados de la semana: "
	leer dias_trabajados
	
	Escribir "Horas extras trabajadas: "
	leer horas_extras_trabajadas	
	
	si dias_trabajados > 0 & dias_trabajados < 7 Entonces
		pago_por_hora = ((sueldo_semanal / 6) / 8)
		horas_normales_trabajadas = dias_trabajados * 8
		sueldo_horas_normales = horas_normales_trabajadas * pago_por_hora
		
		si horas_extras_trabajadas >= 0 & horas_extras_trabajadas < 9 Entonces		
			pago_extra_doble = ((pago_por_hora * horas_extras_trabajadas)*2)
		SiNo
			pago_extra_doble = ((pago_por_hora * 8)*2)
		FinSi
		
		pago_extra_triple = (((horas_extras_trabajadas - 8) * pago_por_hora)*3)
		
		
		si horas_extras_trabajadas >= 0 & horas_extras_trabajadas < 9 Entonces
			pago_total_horas_extras = pago_extra_doble 
		SiNo
			pago_total_horas_extras = pago_extra_doble + pago_extra_triple
		FinSi
	SiNo
		no_valido = "El numero introducido es correcto"
	FinSi
	
	sueldo_total_Horas_Normales_Extras = sueldo_horas_normales + pago_total_horas_extras
	
	si sueldo_total_Horas_Normales_Extras <= 2500 Entonces
		descuento_imss = sueldo_total_Horas_Normales_Extras * .04		
	SiNo
		descuento_imss = sueldo_total_Horas_Normales_Extras * .07		
	FinSi
	
	descuento_imss_final = sueldo_total_Horas_Normales_Extras - descuento_imss
	
	
	Segun dias_trabajados hacer 
		1:
			si horas_extras_trabajadas >= 0 & horas_extras_trabajadas <= 8 Entonces			
				Imprimir "El pago de tus horas normales es de: $", sueldo_horas_normales
				Imprimir "Total del pago de horas extras es de: $" pago_total_horas_extras
				
			SiNo 
				si horas_extras_trabajadas >= 9 & horas_extras_trabajadas <= 16 entonces
					
					Imprimir "El pago de tus horas normales es de: $", sueldo_horas_normales
					Imprimir "Total del pago de horas extras es de: $" pago_total_horas_extras
				SiNo
					Imprimir "No es posible trabajar ", horas_extras_trabajadas ," horas segun los dias trabajados."
				FinSi
			FinSi
		2:
			si horas_extras_trabajadas >= 0 & horas_extras_trabajadas <= 8 Entonces
				
				Imprimir "El pago de tus horas normales es de: $", sueldo_horas_normales
				Imprimir "Total del pago de horas extras es de: $" pago_total_horas_extras
				
			SiNo 
				si horas_extras_trabajadas >= 9 & horas_extras_trabajadas <= 32 entonces
					
					Imprimir "El pago de tus horas normales es de: $", sueldo_horas_normales
					Imprimir "Total del pago de horas extras es de: $" pago_total_horas_extras
				SiNo
					Imprimir "No es posible trabajar ", horas_extras_trabajadas ," horas segun los dias trabajados."
				FinSi
			FinSi
		3:
			si horas_extras_trabajadas >= 0 & horas_extras_trabajadas <= 8 Entonces
				
				Imprimir "El pago de tus horas normales es de: $", sueldo_horas_normales
				Imprimir "Total del pago de horas extras es de: $" pago_total_horas_extras
				
			SiNo 
				si horas_extras_trabajadas >= 9 & horas_extras_trabajadas <= 48 entonces
					
					Imprimir "El pago de tus horas normales es de: $", sueldo_horas_normales
					Imprimir "Total del pago de horas extras es de: $" pago_total_horas_extras
				SiNo
					Imprimir "No es posible trabajar ", horas_extras_trabajadas ," horas segun los dias trabajados."
				FinSi
			FinSi
		4:
			si horas_extras_trabajadas >= 0 & horas_extras_trabajadas <= 8 Entonces
				
				Imprimir "El pago de tus horas normales es de: $", sueldo_horas_normales
				Imprimir "Total del pago de horas extras es de: $" pago_total_horas_extras
				
			SiNo 
				si horas_extras_trabajadas >= 9 & horas_extras_trabajadas <= 64 entonces
					
					Imprimir "El pago de tus horas normales es de: $", sueldo_horas_normales
					Imprimir "Total del pago de horas extras es de: $" pago_total_horas_extras
				SiNo
					Imprimir "No es posible trabajar ", horas_extras_trabajadas ," horas segun los dias trabajados."
				FinSi
			FinSi
		5:
			si horas_extras_trabajadas >= 0 & horas_extras_trabajadas <= 8 Entonces
				
				Imprimir "El pago de tus horas normales es de: $", sueldo_horas_normales
				Imprimir "Total del pago de horas extras es de: $" pago_total_horas_extras
				
			SiNo 
				si horas_extras_trabajadas >= 9 & horas_extras_trabajadas <= 80 entonces
					
					Imprimir "El pago de tus horas normales es de: $", sueldo_horas_normales
					Imprimir "Total del pago de horas extras es de: $" pago_total_horas_extras
				SiNo
					Imprimir "No es posible trabajar ", horas_extras_trabajadas ," horas segun los dias trabajados."
				FinSi
			FinSi
		6:
			si horas_extras_trabajadas >= 0 & horas_extras_trabajadas <= 8 Entonces
				
				Imprimir "El pago de tus horas normales es de: $", sueldo_horas_normales
				Imprimir "Total del pago de horas extras es de: $" pago_total_horas_extras
				
			SiNo 
				si horas_extras_trabajadas >= 9 & horas_extras_trabajadas <= 96 entonces
					
					Imprimir "El pago de tus horas normales es de: $", sueldo_horas_normales
					Imprimir "Total del pago de horas extras es de: $" pago_total_horas_extras
				SiNo
					Imprimir "No es posible trabajar ", horas_extras_trabajadas ," horas segun los dias trabajados."
				FinSi
			FinSi
		De Otro Modo:
			Imprimir no_valido			
			Imprimir  "Ingrese el numero de dias trabajados en un rango de 1-6"
			
	FinSegun	
	
	Imprimir "Tu descuento de imss es de: ", descuento_imss
	Imprimir "Tu desceunto final con imss es de. ", descuento_imss_final
	
FinAlgoritmo
