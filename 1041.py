# entrada
entrance = input()

# extrair valores de x e y
v = entrance.split(' ')
X = float(v[0])
Y = float(v[1])

# condições para descobrir quadrante
if (X == 0) and (Y == 0):
    print('Origem')

elif (X > 0) and (Y > 0):
    print('Q1')

elif (X > 0) and (Y < 0):
    print('Q4')

elif (X < 0) and (Y > 0):
    print('Q2')

elif (X < 0) and (Y < 0):
    print('Q3')

elif (X == 0) and ((Y > 0) or (Y < 0)):
    print('Eixo Y')

elif (Y == 0) and ((X > 0) or (X < 0)):
    print('Eixo X')
