# variaveis
listD = {}
listO = []
count = 1

# 100 entradas
for i in range(100):
    number = int(input())
    listD.update({count: number})
    count = count + 1

# convertendo em uma lista
for j in listD.values():
    listO.append(j)

# colocado em ordem crescente
listO = sorted(listO)

# maior resultado
Bnumber = listO[99]

# a procura da posição
for x, y in listD.items():

    if y == Bnumber:
        print('{}\n{}'.format(y, x))
