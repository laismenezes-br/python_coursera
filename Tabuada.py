#Repetições encaixadas (exemplos de programas que usam tabela - tabuada)

linha = 1
coluna = 1

while linha <= 10:
    while coluna <= 10:
        print(linha * coluna, end = "\t")#end define que print passa para a linha de baixo, mas eu quero espaço em tab
        coluna = coluna + 1
    linha = linha + 1
    print()#para imprimir de 10 em 10
    coluna = 1
