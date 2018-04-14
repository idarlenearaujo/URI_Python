# variavel
entrance = True
listaNumber = []
listaNumberCres = []
listaNumber2 = []
listaSumNumber2 = []
countIntervalo = 0
countLp = 0
vT = 0
counF = 0
m = []

# entrada de pares de numeros ate que digite 0 ou numero negativo
while entrance is True:

    n1, n2 = map(int, input().split(' '))

    if (n1 <= 0) or (n2 <= 0):
        entrance = False
        break
    else:

        # adicionar numeros em uma lista
        listaNumber.append(n1)
        listaNumber.append(n2)

        # ordem crescente
        listaNumberCres = sorted(listaNumber)

        # calcular se existe numeros nesse intervalo e + os numeros do intervalo
        countIntervalo = (listaNumberCres[1] - listaNumberCres[0]) + 1

        # numero inicial
        number = listaNumberCres[0]

        # percorrer o intervalo e armazenar numeros
        while countLp < countIntervalo:

            listaNumber2.append(number)
            number = number + 1
            countLp = countLp + 1

        # soma total do intervalo
        for i in listaNumber2:
            vT = vT + i

        listaSumNumber2.append(vT)

        # matrix
        m.append(listaNumber2)

        # resetando
        listaNumber = []
        listaNumber2 = []
        countLp = 0
        number = 0
        vT = 0

# resultado
while counF < len(listaSumNumber2):

    sequencia = str(m[counF])
    nsequencia = sequencia.replace(',', '').replace('[', '').replace(']', '')
    print(nsequencia, 'Sum={}'.format(listaSumNumber2[counF]))

    counF = counF + 1
