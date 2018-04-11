# entrada v1
v1 = int(input())
# entrada v2
v2 = int(input())
# entrada v3
v3 = int(input())
# entrada v4
v4 = int(input())
# entrada v5
v5 = int(input())

# variaveis
count = 0
listV = []

# adicionar a lista
listV.append(v1)
listV.append(v2)
listV.append(v3)
listV.append(v4)
listV.append(v5)

# percorrer a lista e encontrar numeros pares
for i in listV:

    if i % 2 == 0:
        count = count + 1

print('{} valores pares'.format(count))
