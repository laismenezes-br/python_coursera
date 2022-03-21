#Exercício de fatorial
#Recebe número natural do usuário
n = int(input("Digite o valor de n: "))
#n_fatorial = 1, poispoderia zerar a operação fatorial
n_fatorial = 1
while n >= 1:
    n_fatorial = n_fatorial * n
    n = n - 1
print(n_fatorial)
