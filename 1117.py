# variables
notasV = 0
soma = 0

# while there are not 2 grades between [0,10], so the loop continue
while notasV < 2:

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
