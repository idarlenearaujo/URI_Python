# variavel
count = 0
number = 0.0
i = 0

# entrance intenger
for i in range(6):
    number = float(input())

    # se positivo count++
    if number >= 0:
        count = count + 1

print('{} valores positivos'.format(count))
