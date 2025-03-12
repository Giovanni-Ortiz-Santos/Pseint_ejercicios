Algoritmo Pago_Trabajador
	
	Definir horas, pago, Pago_F, HoraED, HorasT Como Entero
	
	Imprimir '¿Cuantas horas a trabajado en la semana?'
	Leer horas
	Imprimir '¿Cuantas te pagan por hora?'
	Leer pago
	Pago_F = horas * pago
	
	si horas >= 0 & horas < 41 Entonces
		Imprimir 'Tu patrion te debe pagar ', Pago_F, ' pesos'
	SiNo
		si  horas >= 41 & horas <= 45 Entonces
			HoraED = horas -  40;
			Pago_F = (40 * pago) + (HoraED * 2 * pago)
			Imprimir 'Su sueldo final por hacer mas tiempo, es al doble por lo tanto se le dara: ', Pago_F, ' pesos'
		SiNo
			si horas >=46 & horas <=50 Entonces
				HoraED = 5
				HorasT = horas-45
				Pago_F = (pago * 40) + (HoraED * 2 * pago) + (HorasT * 3 * pago)
				Imprimir 'Usted si se sabe la de chambear y por ello le pagaremos: ', Pago_F, ' Pesos'
			SiNo
				Imprimir '¿Acaso no te quieren en tu casa?, No esta permitido trabajar mas de 50 hr a la semana'
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo
