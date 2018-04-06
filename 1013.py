# entrada
values = input()

# extraindo valores
v = values.split(' ')

# armazenando os valores
A = int(v[0])
B = int(v[1])
C = int(v[2])

# calculos
maiorAB = (A + B + abs(A - B))/2
maiorABC = (maiorAB + C + abs(maiorAB - C))/2

print('{:.0f} eh o maior'.format(maiorABC))
