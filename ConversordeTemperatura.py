#conversão de temperatura (Celsius para Fahrenheit)
#C/5 = (F - 32)/9

#comando "input" para entrada do usuário
temperaturaFahrenheit = input("Digite a temperatura: ")
#como "input" é dada por usuário, a variável é string e para evitar erro converte-se para float
temperaturaCelsius = ((float(temperaturaFahrenheit) - 32)*5)/9

print("A temperatura em Celsius é: ",temperaturaCelsius)
