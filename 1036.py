from math import sqrt

# entrada
numbers = input()

# obterndo os inteiros A,B,C,D
v = numbers.split(' ')
A = float(v[0])
B = float(v[1])
C = float(v[2])

# condição para falha
if (A == 0.0) or ((pow(B, 2) - (4 * A * C)) < 0):
    print('Impossivel calcular')

# condição para calcular baskara
else:
    r1 = (-B + sqrt(pow(B, 2) - (4 * A * C))) / (2 * A)
    r2 = (-B - sqrt(pow(B, 2) - (4 * A * C))) / (2 * A)

    print('R1 = {:.5f}\nR2 = {:.5f}'.format(r1, r2))