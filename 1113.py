# variaveis
entrance = True
listResult = []

# entrada de pares de numeros ate que digite n1 = n2
while entrance is True:

    n1, n2 = map(int, input().split(' '))

    # se igual sai
    if n1 == n2:
        entrance = False
        break

    # se numeros diferentes
    else:

        if n1 > n2:
            result = 'Decrescente'
            listResult.append(result)

        elif n2 > n1:
            result = 'Crescente'
            listResult.append(result)

# mostrar resultado
for i in listResult:
    print(i)
