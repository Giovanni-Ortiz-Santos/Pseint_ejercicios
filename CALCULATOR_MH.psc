Algoritmo CALCULATOR_MH
	DEFINIR N1, N2, OP, R Como Real
	Escribir "INGRESA UN N�MERO"
	LEER N1
	Escribir "INGRESA UN SEGUNDO N�MERO"
	LEER N2
		
	SI N1<0 Entonces
		Escribir "NO PUEDES INGRESAR VALORES NEGATIVOS"
		
		SINO SI N2<0 Entonces
				Escribir "NO PUEDES INGRESAR VALORES NEGATIVOS"
			SiNo
				
	ESCRIBIR "ESCOGE LA OPERACI�N QUE DESEAS REALIZAR"
	ESCRIBIR "OPCI�N 1= SUMA"
	ESCRIBIR "OPCI�N 2= RESTA"
	ESCRIBIR "OPCI�N 3= MULTIPLICACI�N"
	ESCRIBIR "OPCI�N 4= DIVISI�N"
	LEER OP
	SI OP=1 Entonces
		R=N1+N2
		SINO
		SI OP=2 ENTONCES
			R=N1-N2
		SINO SI OP=3 Entonces
				R=N1*N2
			SINO SI OP=4 Entonces
					SI N2=0 Entonces
						Escribir "NO PUEDES DIVIDIR ENTRE 0"
					SINO 
						R=N1/N2
					FinSi
				FinSi
			FinSi
		FinSi
	FINSI
	
	SI R<0 Entonces
		Escribir "NO PUEDES OBTENER N�MEROS NEGATIVOS"
	SiNO
		Escribir R
	FinSi
	
FinSi
FINSI 


FinAlgoritmo

	
