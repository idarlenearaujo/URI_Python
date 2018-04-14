# numero de pares a serem realizados a divisao
qnt = int(input())

# divisao dos pares, mas se algum v[2] == 0 {Divisao impossivel}
for i in range(qnt):
    v1, v2 = map(float, input().split(' '))

    # v2 = 0 Divisão impossivel
    if v2 == 0:
        print('divisao impossivel')
    else:
        div = v1 / v2
        print(div)
