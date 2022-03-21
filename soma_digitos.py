#Soma dos dígitos de um inteiro

numero = input("Digite um número inteiro: ")
seq = len(numero)
numero1 = int(numero)
soma = 0

while seq >= 0:
#Para achar o dígito
    d = numero1%10
    i = numero1//10
    numero1 = i
    soma = soma + d
    seq = seq - 1
    
print(soma)
