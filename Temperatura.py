#Lista de temperaturas,imprima a mais fria e a mais quente.
def MinMax(temperaturas):
    print("A menor temperatura do mês foi: ", minima(temperaturas),"Cº.")
    print("A maior temperatura do mês foi: ", maxima(temperaturas),"Cº.")

def maxima(temps):
    max = temps[0] #começa com a primeira temperatura, para quando não hover temps menores que "0".
    i = 1
    while i < len (temps):
        if temps[i] > max:
            max = temps[i] #para atualizar a temperatura de máxima
        i = i + 1
    return max


def minima(temps):
    min = temps[0] #começa com a primeira temperatura, para quando não hover temps menores que "0".
    i = 1
    while i < len (temps):
        if temps[i] < min:
            min = temps[i] #para atualizar a temperatura de mínimo
        i = i + 1
    return min

######  TESTES PADRONIZADOS ######
def teste_pontual(temps,valor_esperado):
    valor_calculado = minima(temps)
    if valor_calculado != valor_esperado:
        print("valor errado", temps)
        print("valor esperado: ", valor_esperado,". valor calculado: ",valor_calculado)
    
def testa_minima():
    print("Iniciando os testes")

    teste_pontual([0], 0)
        
    teste_pontual([0,0,0,0], 0)

    teste_pontual([-2,-3,-8,6,10,20,0], -8)    

    print("Finalizando os testes")
