#Cada número digitado você precisa devolver o fatorial

num = int(input("Digite um número inteiro: "))

while num >= 0:  
    fat = 1
    while num > 1:
        fat = fat * num
        num = num - 1
    print(fat)
    num = int(input("Digite um número inteiro: "))#para sair do laço, caso digite um negativo sai do programa
    
