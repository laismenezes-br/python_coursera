#Exercício 2 (Conta segundos)
númerodeseg_str = input("Por favor, entre com o número de segundos que deseja converter: ")

#Converte a variável de entrada em inteiros
númerodeseg_int = int(númerodeseg_str)

#Para dia (divisão da parte inteira)
dias = númerodeseg_int // (24*3600)

#Horas pega resto da divisão do dia
númeroseg_resto1 = númerodeseg_int % (24*3600)
horas = númeroseg_resto1 // 3600

#Minutos 

númeroseg_resto2= númeroseg_resto1 % 3600
minutos = númeroseg_resto2 //60

#Segundos restantes
segundos = númeroseg_resto2 % 60


print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")
