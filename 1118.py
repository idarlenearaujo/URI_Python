# variables
notasV = 0
soma = 0
looP = True

# while looP is equal True, so the loop continue
while looP is True:

    # receive float
    nota = float(input())

    # if nota is >= 0 and nota <= 10
    if (nota >= 0) and (nota <= 10):
        notasV = notasV + 1
        soma = soma + nota

    # if it is not true
    else:
        print('nota invalida')

    # media
    if notasV == 2:
        soma = soma / 2
        print('media = {:.2f}'.format(soma))

        # receive if user want or not to continue the loop or if x = 2
        opcao = int(input('novo calculo (1-sim 2-nao)\n'))
        while (opcao < 1) or (opcao > 2):
            opcao = int(input('novo calculo (1-sim 2-nao)\n'))

        # end
        if opcao == 2:
            looP = False

        # to be continued
        elif opcao == 1:
            notasV = 0
            soma = 0
