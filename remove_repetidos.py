
def remove_repetidos(lista): 
    lista = lista[:]
    n = len(lista) - 1 
    a = 0

    while a < n :
        while n > a :
            if lista[a] == lista[n]:
                del lista[n]
            n = n - 1
        a = a + 1
        n = len(lista) - 1
    return sorted(lista)#sorted(lista) - organiza por ordem numérica
                        

    
