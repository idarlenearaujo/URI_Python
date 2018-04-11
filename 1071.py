# entrada valor 1 int
value1 = int(input())

# entrada valor 2 int
value2 = int(input())

# variavel
list = []
listI = []
listB = []
soma = 0

# adicionar na lista valores
list.append(value1)
list.append(value2)

# ordem crescente
listB = sorted(list)

# valores
v1 = int(listB[0])
v2 = int(listB[1])

# verificar quais sao impares
for i in range((v1 + 1), v2):

    if i % 2 != 0:
        listI.append(i)

# somando elementos da lista
for j in listI:

    soma = soma + j

print(soma)
