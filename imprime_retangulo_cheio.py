#O usuário fornece largura e a altura, sendo os valores devolvidos por "#"

a = int(input("digite a largura: "))
b = int(input("digite a altura: "))

while b > 0:
    #a variável "a_while" é definida, para o "a" não zerar e continuar o while
    a_while = a
    while a_while > 0:
        print ("#",end = "")
        a_while = a_while - 1
    print ()
    b = b - 1
