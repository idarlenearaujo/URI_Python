# entrance de quantos intervalos
number = int(input())

# variaveis
lista = []
lista2 = []
listaSoma = []
listaFinal = []
countLp = 0
vT = 0

# entrada de valores, classificar, soma
for i in range(number):
    n1, n2 = map(int, input().split(' '))
    lista.append(n1)
    lista.append(n2)
    lista2 = sorted(lista)

    # intervalo entre os numeros
    countN = (lista2[1] - lista2[0]) - 1

    # se existir numeros entre o intervalo digitado
    if countN > 0:

        testNumber = lista2[0] + 1

        # intervalo
        while countLp < countN:

            # se e impar
            if testNumber % 2 != 0:
                listaSoma.append(testNumber)

            # proximo numero do intervalo
            testNumber = testNumber + 1
            countLp = countLp + 1

        # soma do intervalo impar
        for j in listaSoma:
            vT = vT + j

        # armazenando valor total final de um intervalo
        listaFinal.append(vT)

    # caso não exista valores entre o intervalo
    else:

        listaFinal.append(0)

    # resetando
    lista = []
    lista2 = []
    listaSoma = []
    vT = 0
    countLp = 0

# valores finais
for values in listaFinal:
    print(values)
