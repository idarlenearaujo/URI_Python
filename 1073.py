# entrada numero
number = int(input())

# variavel
calc = 0

# calcular pow() até numero digitado
for i in range(1, (number + 1)):
    if i % 2 == 0:
        calc = pow(i, 2)
        print('{}^2 = {}'.format(i, calc))
