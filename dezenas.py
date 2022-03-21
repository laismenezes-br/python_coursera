# Dígito de dezena
valor = input ("Digite um número inteiro: ")

#Converte o valor de entrada
valor_int = int(valor)

#Para obeter os dois últimos dígitos
dezena = (valor_int%100)

#A divisão por inteiro devolve somente o valor da casa da dezena
número_dezena = dezena//10

print("O dígito das dezenas é",número_dezena)
