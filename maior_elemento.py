def maior_elemento(lista): 
    lista = lista[:]
    n = len(lista) - 1 
    a = 0
    numero = 0

    while  n > a:
        if lista[a] >= lista[n]:
            del lista [n]
            n = n - 1
        else:
            del lista [a]
            n = n - 1
            #precisa-se sempre dimunuir o valor de n, pois um elemento da lista é retirado
    numero = lista[0]
    return numero
