# entrada v1
v1 = float(input())
# entrada v2
v2 = float(input())
# entrada v3
v3 = float(input())
# entrada v4
v4 = float(input())
# entrada v5
v5 = float(input())
# entrada v6
v6 = float(input())

# variaveis
count = 0
countJ = 0
media = 0
listV = []
listP = []

# adicionar a lista
listV.append(v1)
listV.append(v2)
listV.append(v3)
listV.append(v4)
listV.append(v5)
listV.append(v6)

# percorrer a lista e encontrar numeros positivos
for i in listV:

    if i >= 0:
        count = count + 1
        listP.append(i)

# percorrer a lista de positivos e calcular a media
for j in listP:
    media = media + j
    countJ = countJ + 1

# media total
mediaT = media / countJ

print('{} valores positivos\n{:.1f}'.format(count, mediaT))
