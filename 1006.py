# entrada 3 float
A = float(input())
B = float(input())
C = float(input())

# variaveis (pesos)
P1 = 2
P2 = 3
P3 = 5

# calculo da media
MEDIA = ((A * P1) + (B*P2) + (C*P3)) / (P1+P2+P3)

print('MEDIA = {:.1f}'.format(MEDIA))
