# variavel
soma = 0
lista = []

# entrada
number1 = int(input())
number2 = int(input())

# adicionando em uma lista para ordenar
lista.append(number1)
lista.append(number2)
lista = sorted(lista)

# percorre intervalo de numeros e soma os numeros que não são divisiveis por 13
for i in range(lista[0], lista[1] + 1):

    # se sobra resta da digisao somar numero
    if i % 13 != 0:
        soma = soma + i

print(soma)
