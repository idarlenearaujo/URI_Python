# entrada de quantos numeros serao lidos
number = int(input())

# variavel
lista = []

# lista de numeros para teste
for i in range(0, number):

    entrance = int(input())
    lista.append(entrance)

# percorrer lista e verificar null, odd negative, odd positivo, even negative
for j in lista:
    # negativo
    if j < 0:
        if j % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')

    # neutro
    elif j == 0:
        print('NULL')

    # positivo
    else:
        if j % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
