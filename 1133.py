# variavel
lista = []
listaI = []

# entrada de dois numeros
number1 = int(input())
number2 = int(input())

# adicionando na lista e ordenando
lista.append(number1)
lista.append(number2)
lista = sorted(lista)

# gerar o intervalo entre os numeros
for i in range((lista[0] + 1), lista[1]):
    # numero nao seja divisivel por 5 e ainda reste 2 ou 3 no resto da divisao
    resto = i % 5
    if (resto == 2) or (resto == 3):
        listaI.append(i)

# mostra resultado
for j in listaI:
    print(j)