#Maior número primo com base no valor recebido
def maior_primo(x):
#Número de sequência da divisão
    seq = 2
    a = 0
#A variável "b" guarda se o resto da divisão nunca foi zero, caso seja ele é o próprio "x" é primo.
    b = 0
    y = 0
    while seq < x:
          a = x%seq
          if a == 0:
             b = b + 1
             seq = seq + 1
          else:
             numero = seq
             seq = seq + 1
#Se a variável "b" for zero o próprio número é o maior primo.    
    if b == 0:
       return (x)
#Caso contrário ele repete o procedimento com a variável "numero" até achar um primo.
    else:
       while b != 0: 
             y = maior_primo(numero)
             return y
        


        
       
