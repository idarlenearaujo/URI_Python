# variaveis
cont = 1
n = 4
ant = 0
lista = []
llinha =[]

# entrada de quantidade de linhas
numberLinha = int(input())

# gera linhas
for i in range(numberLinha):
    # gera valor em cada linha (4 em 4) sendo o ultimo valor = PUM
    for j in range(ant, n):

        if cont < 4:
            lista.append(j+1)

        elif cont > 3:
            lista.append('PUM')

        cont = cont + 1

    ant = n 
    n = n + 4
    llinha.append(lista)
    lista = []
    cont = 1

# leitura do resultado
for value in llinha:
    print(value[0], value[1], value[2], value[3])
