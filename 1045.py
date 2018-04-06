# entrada
entrance = input()

# extrair 3 valores
v = entrance.split(' ')
A = float(v[0])
B = float(v[1])
C = float(v[2])

listNum = []
lista = []
listNum.append(A)
listNum.append(B)
listNum.append(C)

lista = sorted(listNum, reverse=True)

A = lista[0]
B = lista[1]
C = lista[2]

# condição de trianglo ou não
if A >= (B + C):
    print('NAO FORMA TRIANGULO')

else:
    if pow(A, 2) == ((pow(B, 2) + pow(C, 2))):
        print('TRIANGULO RETANGULO')

    if pow(A, 2) > ((pow(B, 2) + pow(C, 2))):
        print('TRIANGULO OBTUSANGULO')

    if pow(A, 2) < ((pow(B, 2) + pow(C, 2))):
        print('TRIANGULO ACUTANGULO')

    if A == B and B == C and C == A:
        print('TRIANGULO EQUILATERO')

    if (A == B and B != C and C != A) or (A != B and B != C and C == A) or (A != B and B == C and C != A):
        print('TRIANGULO ISOSCELES')
