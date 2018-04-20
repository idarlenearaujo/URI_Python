# contadores de 1 - alcool 2 - gasolina 3 - diesel
contA = 0
contG = 0
contD = 0

# loop com entrada de inteiros
while True:
    number = int(input())

    # se o user digitar 4 sai e imprime resumo da operacao
    if number == 4:
        break
    else:
        # se 1 alcool
        if number == 1:
            contA = contA + 1
        # se 2 gasolina
        elif number == 2:
            contG = contG + 1
        # se 3 diesel
        elif number == 3:
            contD = contD + 1

        continue

print('MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}'.format(contA, contG, contD))