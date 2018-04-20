# variaveis
count = 0
listaA = []
listaB = []
vt1 = 0
vt2 = 0
empate = 0

# Loop ate alguem digitar 1 na opcao (Novo grenal (1-sim 2-nao))
while True:
    # placar
    t1, t2 = map(int, input().split(' '))

    # armazenando resultado
    listaA.append(t1)
    listaA.append(t2)
    listaB.append(listaA)

    # contador de grenais
    count = count + 1

    # novo grenal?
    opcao = int(input('Novo grenal (1-sim 2-nao)\n'))

    # se 1 novo grenal
    if opcao == 1:
        listaA = []
        continue

    # se fim, hora de realizar a contagem de vitorias para o t1 e t2 e empates, e claro quem venceu
    else:

        # averigar lista
        for i in listaB:

            if i[0] > i[1]:
                vt1 = vt1 + 1
            elif i[0] < i[1]:
                vt2 = vt2 + 1
            else:
                empate = empate + 1

        if vt1 == vt2:
            result = 'Não houve vencedor'
        elif vt1 > vt2:
            result = 'Inter venceu mais'
        else:
            result = 'Gremio venceu mais'

        # numero de grenais, time 1 vitorias, time 2 vitorias, empate, quem ganhou
        print('{} grenais\nInter:{}\nGremio:{}\nEmpates:{}\n{}'.format(count, vt1, vt2, empate, result))

        # finalizar
        break


