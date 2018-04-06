# entrada
numbers = input()

# obtendo os inteiros A,B,C,D
v = numbers.split(' ')
A = int(v[0])
B = int(v[1])
C = int(v[2])
D = int(v[3])

# condição
if (C >= 0) and (D >= 0) and (A % 2 == 0) and (B > C) and (D > A) and ((C + D) > (A + B)):
    print('Valores aceitos')

else:
    print('Valores nao aceitos')
