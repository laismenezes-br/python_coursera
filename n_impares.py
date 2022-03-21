#Números primos
n = int (input("Digite o valor de n: "))
x = 1
# Recebe um número inteiro positivo
while n > 0 :
    if x % 2 != 0:
       print (x)
    #Para ver os ímpares "x" passa de dois em dois e o valor de "n" diminui 
    x = x + 2        
    n = n - 1



    
