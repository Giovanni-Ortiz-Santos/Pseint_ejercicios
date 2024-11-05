Algoritmo Menu_Operaciones	
	Imprimir "*** Menu de operaciones ***"
	Imprimir "Seleccione con un numero la operacion que desee"
	Imprimir "1: z^2 = x^2 + m^2"
	Imprimir "2: Par o impar "	
	Imprimir "3: 10 tablas de multiplicar"
	Imprimir "4: Otorga 3 valores menor a mayor"
	Imprimir "5: Factorial de x numero"
	Imprimir "6: Serie fibonasi hasta x numero"
	Leer opc	
	Segun opc Hacer
		1: 
			Imprimir 'ingresa el valor de z'
			Leer cal
			z<-1
			Mientras z<=cal Hacer
				x<-1
				Mientras x<=z Hacer
					c<-1
					mientras c<=z Hacer
						si (x^2 + c^2 = z^2) Entonces
							Imprimir  'solucion encontrada ',x,"^2 + ",c,"^2 = ",z,"^2"
						FinSi
						c<-c+1
					FinMientras
					x<-x+1
				FinMientras
				z<-z+1
			FinMientras
		2:
			Imprimir "Ingresa un numero: "
			Leer numIngresado			
			si numIngresado % 2 == 0 Entonces
				Imprimir "El numero ", numIngresado," es un numero par"
			SiNo
				Imprimir "El numero ",numIngresado ," es un numero impar"
			FinSi			
		3:
			a = 1			
			Mientras a <= 10 Hacer
				b = 1
				Mientras  b <= 10
					r = b * a
					Imprimir a, ' * ' , b, " = " r
					b = b + 1
				FinMientras				
				Imprimir  "Pulsa enter por contador "
				Leer z
				Borrar Pantalla
				a = a + 1
			FinMientras
		4:
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
						Imprimir n3, "/ ", n2 ,"/ ", n1
					SiNo
						Imprimir n1,'/ ',n2,'/ ',n3
					FinSi
				FinSi				
			SiNo
				si n1 > n2 Entonces
					si n1 > n3 Entonces
						si n2 > n3 Entonces
							Imprimir n3, '/ ',  n2, '/ ',  n1
						SiNo
							Imprimir n2,'/ ',  n3, '/ ',  n1
						FinSi
					SiNo
						Imprimir n2, '/ ', n1, '/ ', n3
					FinSi
				SiNo
					si n2 > n3 Entonces
						si n1 > n3 Entonces
							Imprimir n3, '/ ', n1, '/ ', n2
						SiNo
							Imprimir n1, '/ ',  n3, '/ ', n2
						FinSi
					SiNo
						Imprimir n1, '/ ',  n2,'/ ', n3
					FinSi
				FinSi				
			FinSi
		5:
			Imprimir "numero final a obtener factorial"
			Leer x
			c = 1
			r = 1					
			Mientras c <= x Hacer
				r = r * c 
				Imprimir (r/c) "*" c "=" r 
				c = c + 1
			FinMientras					
		6:
			Imprimir  'digite el final de la serie fibonasi'
			Leer x
			a = 0 
			b = 1
			c = 0
			cont = 0			
			Mientras  cont <= x Hacer
				imprimir cont ,' / ', c 
				a = b
				b = c
				c = a + b
				cont = cont + 1
			FinMientras			
		De Otro Modo:
			Imprimir "No existe numero para la operacion :(, intente de nuevo :)"			
	FinSegun	
FinAlgoritmo
