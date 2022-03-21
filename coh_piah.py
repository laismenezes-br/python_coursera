#Similaridades entre texto COH - PIAH:

import re #Biblioteca de expressões regulares - especifica as regras para o conjunto de strings possíveis

###### Dados de assinatura ######

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.\nInforme a assinatura típica de um aluno infectado:\n")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]
    

###### Texto para comparação ######
def le_textos():
    
    i = 1
    textos = []
    texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)#Inclui na lista o texto digitado pelo usuário
        i = i + 1
        texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair):")

    return textos

###### Separação de sentenças ######
def separa_sentencas(texto):

    sentencas = re.split(r'[.!?]+', texto)#A lista é dividida sempre que encontrado detalhes (.!?)
    if sentencas[-1] == '':#Para espaços (" ")
        del sentencas[-1]
    return sentencas

###### Separação de frases ######
def separa_frases(sentenca):

    return re.split(r'[,:;]+', sentenca) #A lista é dividida sempre que encontrado detalhes (,:;)

###### Separação de palavras ######
def separa_palavras(frase):
    return frase.split()#A lista de frases é dividida em palavras

###### Palavras que aparecem somente uma vez ######
def n_palavras_unicas(lista_palavras):
    
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

###### Palavras diferentes ######
def n_palavras_diferentes(lista_palavras):
    
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)
        

def calcula_assinatura(texto):
        
###### Tamanho médio de sentença ######
#Tamanho médio de sentença:números de caracteres em todas as sentenças/
#/número de sentenças
    
    sentencas = separa_sentencas(texto) #Vetor com as sentenças do texto.
    
    #Divisão de caracteres
    i = 0
    y = []       
    while i < len(sentencas):
        y = y + list(sentencas[i])
        i = i+1
    sal_1 = len(y)/len(sentencas)
    
###### Tamanho médio de frase ######
#Tamanho médio de frase:soma de caracteres em cada frase/número de frases
    
    j = 0
    sentenca = [] #Vetor com as frases em cada sentença.
    while j < len(sentencas):
        sentenca = sentenca + separa_frases(sentencas[j])
        j = j+1

    #Divisão de caracteres
    i = 0
    y = []
    while i < len(sentenca):
        y = y + list(sentenca[i])
        i = i+1
    
    pal_1 = len(y)/len(sentenca)

    
###### Complexidade de sentença ######
#Complexidade de sentença:número total de frases/número total de sentenças

    sac_1 = len(sentenca)/len(sentencas)

###### Tamanho médio ######
#Tamanho médio:soma dos tamanhos das palavras/número total de palavras
    
    j = 0
    frase = [] #Vetor com as palavras em cada frase.
    while j < len(sentenca):
        frase = frase + separa_palavras(sentenca[j])
        j = j+1

    #Divisão de caracteres
    i = 0
    y = []
    while i < len(frase):
        y = y + list(frase[i])
        i = i+1
    
    
    wal_1 = len(y)/len(frase)

###### Type-Token ######
#Type-Token:número de palavras diferentes/número total de palavras
    
    lista_palavras = n_palavras_diferentes(frase) #Inteiro devolvido pela função de separação de palavras diferentes

    ttr_1 = lista_palavras/len(frase)
    
###### Hapax Legomana ######
#Hapax Legomana:palavras que aparecem 1 vez/número total de palavras

    unicas = n_palavras_unicas(frase) #Inteiro devolvido pela função de separação de palavras q aparecem uma única vez

    hlr_1 = unicas/len(frase)


    return [wal_1,ttr_1,hlr_1,sal_1,sac_1,pal_1]

def compara_assinatura(as_a, as_b):
#IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    #Grau de similaridade
    soma_absoluta = 0
    i = 0
    while i < 6:
        soma_absoluta = soma_absoluta + (abs(as_a[i] - as_b[i]))
        i += 1
        
    return soma_absoluta/6

def avalia_textos(textos, ass_cp):
#IMPLEMENTAR.
#Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.
#Quanto mais similar menor é o valor de comparação
    inf = []#Vetor com a comparação de assinaturas
    
    for texto in textos:
       as_b = calcula_assinatura(texto)
       inf.append(compara_assinatura(ass_cp,as_b))

    menor = inf[0] #Tomamos o primeiro elemento como menor
    n = 1

    for i in range(1, len(inf)):
        if (menor < inf[i]):
            n = i
    return n
        

def main():    
    ass_cp = le_assinatura()
    textos = le_textos()
    n = avalia_textos(textos, ass_cp)
    print("O autor do texto",n,"está infectado com COH-PIAH")
    
main()
    
    







