# entrada salario
salary = float(input())

# variavel
si = 0
sf = 0
soma = 0.0
sf1 = 0
sf2 = 0
sf3 = 0

# condição valor a pagar por categorias
# não paga
if 0 <= salary <= 2000:
    print('Isento')

# condição 0.8 / 0.18 / 0.28
else:

    # salario > 2000 <= 3000
    if 2000.01 <= salary <= 3000:
        si = salary - 2000
        sf = si * 0.08

        soma = sf

    # salario > 3000 <= 4500
    elif 3000.01 <= salary <= 4500:
        si = salary - 2000
        sf1 = 1000 * 0.08
        sf2 = (salary - (2000 + 1000)) * 0.18

        soma = sf1 + sf2

    # salario > 4500
    elif salary > 4500:
        si = salary - 3000
        sf = (salary - 2000 - si) * 0.08
        sf2 = (4500 - (2000 + (salary - 2000 - si))) * 0.18
        sf3 = (salary - (2000 + (salary - 2000 - si) + ((4500 - (2000 + (salary - 2000 - si)))))) * 0.28

        soma = sf + sf2 + sf3

    print('R$ {:.2f}'.format(soma))
