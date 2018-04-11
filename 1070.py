# entrada valor intenger
value = int(input())

# variavel
count = 0
i = value + 1

# mostrar 6 numeros seguidos impares
while count < 6:

    # impar
    if i % 2 != 0:
        print(i)
        count = count + 1
        i = i + 1
    # se par adiciona +1 no contador
    else:
        i = i + 1
