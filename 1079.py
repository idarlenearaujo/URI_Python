# numeros de casos
entrance = int(input())

# variavel
countC = 0
listaP = []
p1 = 2
p2 = 3
p3 = 5

# calcular media
while countC < entrance:

    a1, a2, a3 = map(float, input().split(' '))
    mediaP = ((a1 * p1) + (a2 * p2) + (a3 * p3))/(p1 + p2 + p3)
    listaP.append(mediaP)

    countC = countC + 1

# imprimir media
for i in listaP:
    print('{:.1f}'.format(i))
