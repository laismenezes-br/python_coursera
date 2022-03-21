def é_hipotenusa(n):
    i = 1
    j = 1
    h = 0


    while i < n:
        while j < n:
            if n*n == i*i + j*j:
                h = h + 1
                return h
            else:
                j = j + 1
        j = 1
        i = i + 1
    return h

def soma_hipotenusas(n):
    soma = 0
    
    while n >= 1:
        h = é_hipotenusa(n)
        
        if h == 1:
            soma = soma + n
        n = n - 1
    return soma
        
