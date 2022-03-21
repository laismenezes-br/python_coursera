#Número com dois dígitos adjacentes iguais
#Variáveis booleanas como indicadores de passagem

numero = input("Digite um número inteiro: ")
#Conta o número de dígitos
dígitos = len (numero)
numero_int = int(numero)
seq = 0
seq1 = 0

iguais = False
while dígitos != 0 and numero_int != 0 and not iguais:
    #Primeiro dígito
    seq = numero_int % 10
    numero_int = numero_int // 10
    seq1 = numero_int % 10
    if seq == seq1:
       iguais = True
       print ("sim")
    dígitos = dígitos - 1
if iguais == False:
    print("não")

        


