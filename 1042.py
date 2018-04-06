# entrada
entrance = input()

# extrair 3 valores inteiros
v = entrance.split(' ')
A = int(v[0])
B = int(v[1])
C = int(v[2])

# variavel
listNumber = []

# adicionando numeros a uma lista
listNumber.append(A)
listNumber.append(B)
listNumber.append(C)

# ler lista em ordem
for i in sorted(listNumber):
    print('{}'.format(i))

print('')

# ler lista como escrito
for i in listNumber:
    print('{}'.format(i))
