#O usuário fornece largura e a altura, sendo os valores devolvidos por "#"
#No entando, dessa vez os que não estiverem na porda do triângulo são espaços

a = int(input("digite a largura: "))
b = int(input("digite a altura: "))

#a variável "b_while" é definida para as bordas
b_while = b

while b_while > 0:
    
    if b_while == b or b_while == 1:
    #a variável "a_while" é definida para o "a" não zerar e continuar o while
        a_while = a
        while a_while > 0:
            print ("#",end = "")
            a_while = a_while - 1
        print ()
        
    else:
        a_while = a
        while a_while > 0:
            if a_while == a or a_while == 1:
                print ("#",end = "")
            else:
                print(" ", end = "")
            a_while = a_while - 1
        print ()
    b_while = b_while - 1
        

