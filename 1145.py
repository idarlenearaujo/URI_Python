# variaveis
cont = 1
lista = []
llinha = []

# entrada numero de colunas e numero final
numColunas, numFinal = map(int, input().split(' '))

numLinhas = numFinal // numColunas

# numero de linhas
for i in range(numLinhas):
    # numero colunas
    for j in range(numColunas):
        lista.append(cont)
        cont = cont + 1

    llinha.append(lista)
    lista = []

# mostra resultado
for values in llinha:
    values = str(values)
    values = values.replace('[', '').replace(']', '').replace(',', '')
    print(values)
