#Jogo NIM (nesse jogo o computador sempre ganha)
#Função principal para escolher o tipo de jogo
def main ():    
    print("Bem-vindo ao jogo do NIM! Escolha: ")
    print("\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato")

    x = int(input(""))
    if x == 1:
        print("\nVocê escolheu uma partida isolada!")
        partida()
    if x == 2:
        print("\nVocê escolheu um campeonato!")
        campeonato()

#Jogo em estilo de campeonato (3 partidas para validar a vitória)                
def campeonato ():
    print ("\n**** Rodada 1 ****")
    partida ()
    c = 1
    u = 0
    print ("\n**** Rodada 2 ****")
    partida ()
    c = c + 1
    print ("\n**** Rodada 3 ****")
    partida ()
    c = c + 1
    print ("\n**** Final do campeonato! ****")
    print ("\nPlacar: Você", u ,"x", c ,"Computador")
    
#Partida isolada (escopo principal do jogo)         
def partida():
    n = int (input("\nQuantas peças? "))
    m = int (input("Limite de peças por jogada? "))
    
    if n % (m+1) != 0 or n <= m:
        print ("\nComputador começa!")

        while n > 0:
            #A variável "x" é para a entrada na função do computador
            x = computador_escolhe_jogada (n,m)
            n = n - x
            print("\nO computador tirou",x,"peças.")
            if n > 0:
                print("Agora resta",n,"peças no tabuleiro.")
                #A variável "y" é para a entrada na função do usuário
                y = usuario_escolhe_jogada (n,m)
                n = n - y
                print("\nVocê tirou",y,"peças.")
                print("Agora resta",n,"peças no tabuleiro.")
        if n == 0:
            print ("Fim de jogo! O computador ganhou!")        
    else:
        print("\nVocê começa!")

        while n > 0:    
            y = usuario_escolhe_jogada (n,m)
            n = n - y
            print("\nVocê tirou",y,"peças.")
            print("Agora resta",n,"peças no tabuleiro.")
            x = computador_escolhe_jogada (n,m)
            n = n - x
            print("\nO computador tirou",x,"peças.")
            if n > 0:
                print("Agora resta",n,"peças no tabuleiro.")
            else:
                print ("Fim de jogo! O computador ganhou!")

            
def computador_escolhe_jogada (n,m):    
    if n <= m: 
       x = n
       return x
    
    else :
        x =  n % (m+1)
        if x > 0:
            return x
    x = m
    return x
        
def usuario_escolhe_jogada (n,m):
    y = int(input("\nQuantas peças você vai tirar? "))
    
    if y <= m and y < n and y >= 1 :
        return y    
    else:
        print("\nOops! Jogada inválida! Tente de novo.")
    return usuario_escolhe_jogada (n,m)

main()


   
     
