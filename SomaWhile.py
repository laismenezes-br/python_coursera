#Soma de números pelo usuário

seq = int(input("Quantos números tem a sequência de soma desejada: "))
soma = 0
valor = 0
while seq != 0:
    valor = int(input("Digite um número para ser somado: "))
    soma = soma + valor
    seq = seq - 1
print ("O valor da soma é",soma)
