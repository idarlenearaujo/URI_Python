# 3 x I e 3 X J
J = 0
I = 0
count = 0

# enquanto não imprimir tudo não sai do laço
while I < 2.1:
    for i in range(3):
        I = I
        J = J + 1
        if (I == 0.0) or (I == 1.0) or (I == 2.0) and (J == 1.0) or (J == 2.0) or (J == 3.0) or (J == 4.0) or (J == 5.0):
            print('I={:.0f} J={:.0f}'.format(I, J))
        else:
            print('I={:.1f} J={:.1f}'.format(I, J))

    I = I + 0.2
    J = 0.2
    count = count + 1

    if count > 0:
        J = 0.2 * count
