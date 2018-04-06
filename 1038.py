# entrada
numbers = input()

# extraindo valores X e Y
v = numbers.split(' ')
X = int(v[0])
Y = int(v[1])

# variaveis
price = 0.00

# condição para preço
if X is 1:
    price = 4.00

# condição para preço
elif X is 2:
    price = 4.50

# condição para preço
elif X is 3:
    price = 5.00

# condição para preço
elif X is 4:
    price = 2.00

# condição para preço
elif X is 5:
    price = 1.50

Total = Y * price

print('Total: R$ {:.2f}'.format(Total))
