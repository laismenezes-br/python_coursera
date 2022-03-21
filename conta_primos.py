#Função que indica a quantidade de primos de um número > 2

def n_primos(n):
    denominador = 2
    b = 0
       
    while n >= 2:
        while denominador <= n:
            if n % denominador == 0:
                n = n - 1
            else:
                denominador = denominador + 1
        b = b + 1
        denominador = 2
            
    return b


