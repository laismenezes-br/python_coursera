#Programa da fórmula de bhaskara
# a*(x**2) + b*(x) + c
# delta = (b)**2 - 4 * a *c
import math
def delta (a,b,c):
    return (b)**2 - 4 * a * c
def main ():
    a_digitado = float (input ("Entre com o valor de a: "))
    b_digitado = float (input ("Entre com o valor de b: "))
    c_digitado = float (input ("Entre com o valor de c: "))
    imprime_raizes (a_digitado,b_digitado,c_digitado)
       
def imprime_raizes(a,b,c):
    d = delta (a,b,c)
    if d < 0:
        print ("esta equação não possui raízes reais")

    if d == 0:
        x = - b / 2*a
        print ("a raiz desta equação é",x)

    if d > 0:
        x = (- b + math.sqrt(d))/ 2*a
        y = (- b - math.sqrt(d))/ 2*a
        if (x <= y):
            print ("as raízes da equação são",x,"e",y)
        else:
            print ("as raízes da equação são",y,"e",x)
