#Programa para verificar se um número é primo, somente divísivel por "1" e por ele mesmo.
numero = int(input("Digite um número inteiro: "))
#O número da sequência de divisão começa por "2" porque pretende avaliar se é divísivel por outros números
seq = 2
a = 0
while seq < numero:
    a = numero%seq
    if a == 0:
       print("não primo")
       seq = numero 
    seq = seq + 1
if seq == numero:
    print("primo")
      
