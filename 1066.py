# entrada v1
v1 = int(input())
# entrada v2
v2 = int(input())
# entrada v3
v3 = int(input())
# entrada v4
v4 = int(input())
# entrada v5
v5 = int(input())

# variaveis
countP = 0
countI = 0
countM = 0
countN = 0
listV = []

# adicionar a lista
listV.append(v1)
listV.append(v2)
listV.append(v3)
listV.append(v4)
listV.append(v5)

# percorrer a lista e encontrar numeros positivos e negativos dentre eles classificar em pares e impares
for i in listV:

    # positivo
    if i > 0:
        countM = countM + 1

        # par
        if i % 2 == 0:
            countP = countP + 1

        # impar
        else:
            countI = countI + 1

    # 0 e par
    elif i == 0:
        countP = countP + 1

    # negativo
    elif i < 0:
        countN = countN + 1

        # par
        if i % 2 == 0:
            countP = countP + 1

        # impar
        else:
            countI = countI + 1

print('{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)'.format(countP, countI, countM, countN))
