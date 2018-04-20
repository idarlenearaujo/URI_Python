# variaveis
num = 1
lista = []
lista2 = []
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

    llinha.append(lista)
    # segunda linha sempre 1 item =, segundo e terceiro + 1 em relacao ao anterior da mesma linha
    lista2 = [lista[0], (lista[1] + 1), (lista[2] + 1)]
    llinha.append(lista2)
    lista = []
    lista2 = []
    num = num + 1

# leitura do resultado
for i in llinha:
    print(i[0], i[1], i[2])
