def soma_elementos(lista):
    lista = lista[:]
    n = len(lista) - 1
    soma = 0
    
    while n >= 0:
        soma = soma + lista[n] 
        n = n - 1
    return soma
