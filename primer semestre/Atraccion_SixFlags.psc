Algoritmo Atraccion_SixFlags
	
	Definir Cost_A, Cost_N, edad, Descuento, Cost_FA, Cost_FN Como Entero
	Definir entrar Como Caracter
	Definir Calificacion Como Real
	
	Cost_A = 1800
	Cost_N = 1200
	
	Imprimir 'Bienveido a Nadando con delfines de Six Flags México'
	Imprimir '¿Desea comprar una entrada para la atraccion?'
	Leer entrar
	
	si entrar = "si" | entrar = "yes"
		Imprimir '¿Cual es tu edad?'
		Leer edad
		
		si edad >= 0 & edad < 18 Entonces
			Imprimir 'Buenas mocoso malcriado, ¿Cual fue tu promedio de último ciclo escolar ?'
			leer Calificacion
			
			si Calificacion >= 9 & Calificacion <= 10
				Descuento = (Cost_N / 100) * 50
				Cost_FN = Cost_N - Descuento
				
				Imprimir 'Bien hecho huerco tus esfuerzos han dado su fruto, por ello solo pagaras:  ', Cost_FN, ' Billuyos'
				Imprimir 'Por ser un buen estudiante te regalamos una foto con la focas'
			SiNo
				Imprimir 'nimodo mocoso pagas ', Cost_N,  ' bolas'
			FinSi
			
		SiNo
			si edad >= 18 & edad < 65 Entonces
				Imprimir 'Orale papi chulo caigale con la feria, su total es de ', Cost_A, ' Doloramas'
				
			SiNo
				si edad >= 65 & edad <= 120 Entonces
					Descuento = (Cost_A / 100) * 40
					Cost_FA = Cost_A - Descuento
					Imprimir 'Buenas tardes señor dinosaurio por su edad se le cobrara solamente: ', Cost_FA, ' money'
				SiNo
					Imprimir 'Sospechoso, no mienta, intente de nuevo'
				FinSi
			FinSi
			
		FinSi
		
	SiNo
		Imprimir 'Que tenga un buen dia :))'
	FinSi
	
	
FinAlgoritmo
