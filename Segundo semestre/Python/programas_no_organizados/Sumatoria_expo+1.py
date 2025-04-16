# Sumatoria de n=n y k = , sumatoria k con:
# Sumatoria de exponentes n = n+1 entre n

#variables
a = 1
n_valor = int(input("Dime el numero de sumatoria que nesesites: "))
sumatoria = 0

while a <= n_valor:
    n_valor_exponente = a**(a+1)
    print(f"{a}^{(a+1)} = {n_valor_exponente}")
    sumatoria = n_valor_exponente + sumatoria
    a = a +1
    
print("La sumatoria de los valores es de: ",sumatoria)
print(f"La divion de los valores es de {(sumatoria / n_valor)}")
