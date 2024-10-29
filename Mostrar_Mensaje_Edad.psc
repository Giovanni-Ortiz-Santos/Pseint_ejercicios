Algoritmo sin_titulo
	Definir n1 Como Entero;
	imprimir "Dame tu edad en años";
	leer n1;
	
	si n1 <= 2 Entonces
		Imprimir "Eres un bebe"
	SiNo
		si n1 > 2 y n1 < 18 Entonces
			Imprimir  "Eres un niño (a)";			
		SiNo
			si n1 > 2 y n1 < 18 Entonces
				Imprimir  "Eres un niño (a)";			
			sino 
				si n1 >= 18 y n1 < 30 Entonces
					Imprimir "Eres Joven"
				sino 
					si n1 >= 30 y n1 < 50 Entonces	
						Imprimir  "Eres un señor"
					SiNo
						si n1 >= 50 y n1 < 60 Entonces
							Imprimir "Eres susegro (ra)"
						SiNo
							si n1 >= 60 y n1 < 70 Entonces
								Imprimir "Eres Abuelito (a)"
							SiNo
								si n1 >= 70 Entonces
									Imprimir "Felicidades por tener una edad mayor a 70 años"
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo
