# entrada
value = int(input())

# variaveis
cashier = True
valueI = value
n1 = 0
n2 = 0
n5 = 0
n10 = 0
n20 = 0
n50 = 0
n100 = 0

# laço quando cashier == False sai
while cashier == True:

    # condicionais
    if value >= 100:

        valueA = value // 100
        n100 = valueA
        valueB = valueA * 100
        value = value - valueB

    # condicionais
    elif value >= 50:

        valueA = value // 50
        n50 = valueA
        valueB = valueA * 50
        value = value - valueB

    # condicionais
    elif value >= 20:

        valueA = value // 20
        n20 = valueA
        valueB = valueA * 20
        value = value - valueB

    # condicionais
    elif value >= 10:

        valueA = value // 10
        n10 = valueA
        valueB = valueA * 10
        value = value - valueB

    # condicionais
    elif value >= 5:

        valueA = value // 5
        n5 = valueA
        valueB = valueA * 5
        value = value - valueB

    # condicionais
    elif value >= 2:

        valueA = value // 2
        n2 = valueA
        valueB = valueA * 2
        value = value - valueB

    # condicionais
    elif value >= 1:

        valueA = value // 1
        n1 = valueA
        valueB = valueA * 1
        value = value - valueB

    # condicionais
    elif value == 0:

        # condição para sair
        cashier = False

print(
    '{}\n{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00\n{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00\n{} nota(s) de R$ 1,00'.format(
        valueI, n100, n50, n20, n10, n5, n2, n1))