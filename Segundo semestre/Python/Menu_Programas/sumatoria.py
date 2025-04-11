class Sumatoria:
    def sumatoria_espo(self,n_valor_tipo):
        a = 1        
        sumatoria = 0
        while a <= n_valor_tipo:
            n_valor_exponente = a**(a+1)
            print(f"{a}^{(a+1)} = {n_valor_exponente}")
            sumatoria = n_valor_exponente + sumatoria
            a = a +1
        return sumatoria