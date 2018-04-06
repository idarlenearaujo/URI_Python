# entrada
entrance = input()

#extrair 2 inteiros
v = entrance.split(' ')
A = int(v[0])
B = int(v[1])

# condição
if A > B:
    ht = (24 - A) + B

elif A < B:
    ht = B - A

elif A == B:
    ht = 24

print('O JOGO DUROU {} HORA(S)'.format(ht))
