Algoritmo Pelicula 
	
	
	Definir Pri_pe, Seg_pe, Ter_pe Como Entero 
	Imprimir 'Ingrese el costo de la primera pelicula'
	leer Pri_pe 
	Imprimir 'Ingrese el costo de la segunda pelicula'
	Leer Seg_pe
	Imprimir 'Ingrese el costo de la tercera pelicula'
	Leer Ter_pe
	
	Si Pri_pe == Seg_pe Entonces
		si Pri_pe == Seg_pe
			CostF = Pri_pe + Seg_pe
			Imprimir 'los costos son iguales por lo tanto el precio a pagar por las tres peliculas son: ', CostIg, ' pesos '
		SiNo
			si Pri_pe > Ter_pe Entonces
				CostF = Pri_pe + Ter_pe
				Imprimir 'las peliculas mas baratas son: ', Pri_pe, '$ ', Ter_pe, '$ por lo tanto deberas pagar ', CostF,'$'
			SiNo
				CostF = Pri_pe +Seg_pe
				Imprimir 'las peliculas mas baratas son: ', Pri_pe, '$ ', Seg_pe, '$ por lo tanto deberas pagar ', CostF,'$'
			FinSi
		FinSi
	SiNo
		si Pri_pe > Seg_pe Entonces
			si Pri_pe > Ter_pe Entonces
				CostF = Seg_pe + Ter_pe
				Imprimir 'las peliculas mas baratas son: ', Seg_pe, '$ ', Ter_pe, '$ por lo tanto deberas pagar ', CostF,'$'
			SiNo
				CostF = Pri_pe + Seg_pe
				imprimir 'las peliculas mas baratas son: ', Pri_pe, '$ ', Seg_pe, '$ por lo tanto deberas pagar ', CostF,'$'
			FinSi
		SiNo
			si Seg_pe > Ter_pe Entonces
				CostF = Pri_pe + Ter_pe
				Imprimir 'las peliculas mas baratas son: ', Pri_pe, '$ ', Ter_pe, '$ por lo tanto deberas pagar ', CostF,'$'
			SiNo
				CostF = Pri_pe + Seg_pe
				Imprimir 'las peliculas mas baratas son: ', Pri_pe, '$ ', Seg_pe, '$ por lo tanto deberas pagar ', CostF,'$'
			FinSi
		FinSi
	FinSi
FinAlgoritmo
