# entrada
entrance = input()

# extrair 3 valores pontos flutuantes
v = entrance.split(' ')
A = float(v[0])
B = float(v[1])
C = float(v[2])

# condição para calcular perímetro do triangulo
if ((B + C) > A) and ((A + B) > C) and ((A + C) > B):
    P = A + B + C
    print('Perimetro = {:.1f}'.format(P))

# condição para calcular area de um trapezio
else:
    A = ((A + B) * C) / 2
    print('Area = {:.1f}'.format(A))
