x = int (input("Digite um número: "))
lista = []
n = 0

while x > 0:    
    lista.append(x)
    x = int (input("Digite um número: "))
sorted (lista)
n = len (lista) - 1
while n >= 0:
    print(lista[n])
    n = n - 1
