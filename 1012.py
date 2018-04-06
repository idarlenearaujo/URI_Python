# entrada
values = str(input())

# extraindo valores
v = values.split(' ')

# armazenando nas variaveis
A = float(v[0])
B = float(v[1])
C = float(v[2])

# variavel
pi = 3.14159

# calculos
TRIANGULO = (A * C)/2
CIRCULO = pi * (C * C)
TRAPEZIO = ((A + B) / 2) * C
QUADRADO = B * B
RETANGULO = A * B

print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}'.format(TRIANGULO, CIRCULO, TRAPEZIO, QUADRADO, RETANGULO))
