# I 3 x de um em um até 9 e o J repete a sequencia 7,6,5
J = 8
I = 1
countCI = 0

# enquanto não imprimir tudo não sai do laço
while countCI < 5:
    for i in range(3):
        I = I
        J = J - 1
        print('I={} J={}'.format(I, J))

    countCI = countCI + 1
    I = I + 2
    J = 8
