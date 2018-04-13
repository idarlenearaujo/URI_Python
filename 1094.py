# numero de testes
number = int(input())

# variavel
ListT = []
qntC = 0
qntS = 0
qntR = 0
qntT = 0
percC = 0
percR = 0
percS = 0

# entrada dos testes
for i in range(number):
    testAnimal = input()
    ListT.append(testAnimal)

# percorrer a lista e categorizando
for j in ListT:
    v = j.split(' ')
    number = int(v[0])
    name = v[1]

    if name == 'C':
        qntC = qntC + number

    elif name == 'S':
        qntS = qntS + number

    elif name == 'R':
        qntR = qntR + number

# soma das categorias
qntT = qntR + qntC + qntS

# calculando percentual de cada categoria
percC = (qntC / qntT) * 100
percR = (qntR / qntT) * 100
percS = (qntS / qntT) * 100

print('Total: {} cobaias\nTotal de coelhos: {}\nTotal de ratos: {}\nTotal de sapos: {}\nPercentual de coelhos: {:.2f} %\nPercentual de ratos: {:.2f} %\nPercentual de sapos: {:.2f} %'
      .format(qntT, qntC, qntR, qntS, percC, percR, percS))
