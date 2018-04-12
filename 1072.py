# entrada de quantos numeros serao lidos
number = int(input())

# variavel
lista = []
countIn = 0
countOut = 0

# lista de numeros para teste
for i in range(0, number):

    entrance = int(input())
    lista.append(entrance)

# percorrer lista e verificar dentro e fora [10,20]
for j in lista:
    if 10 <= j <= 20:
        countIn = countIn + 1
    else:
        countOut = countOut + 1

print('{} in\n{} out'.format(countIn, countOut))
