Algoritmo Login
	
	Definir  UserStore, PasswordStore, User, Password Como Caracter
	
	UserStore = "Goloza303"
	PasswordStore = "PapitasDelSol"
	
	Imprimir 'Bienvenido Usuario ingrese su Nombre de Usuario:'
	Leer User
	Imprimir 'Ingrese su Contraseņa'
	Leer Password
	
	si User == UserStore Entonces
		si PasswordStore == Password
			Imprimir 'Bienvenido. Cecion Iniciada'
		SiNo
			Imprimir 'Usuario o contraseņa incorrectos'
		FinSi
	SiNo
		Imprimir 'captura nuevamente tu usuario'
	FinSi
	
	
FinAlgoritmo
