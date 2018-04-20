# variaveis
num = 1
lista = []
llinha = []

# entrada numero de linhas
number = int(input())

# numero de linhas
for i in range(number):
    # numero de numeros em cada linha
    for j in range(3):
        # potencia
        result = pow(num, j + 1)
        lista.append(result)

    num = num + 1
    llinha.append(lista)
    lista = []

# leitura do resultado
for i in llinha:
    print(i[0], i[1], i[2])
