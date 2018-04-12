# entrada numero
number = int(input())

# variavel
mult = 0

# calculo multiplicando 1 - 10 ao number
for i in range(1, 11):
    mult = i * number
    print('{} x {} = {}'.format(i, number, mult))
