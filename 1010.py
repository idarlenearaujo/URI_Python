# entrada
VP1 = input()
VP2 = input()

# extrair os valores
v1 = VP1.split(' ')
v2 = VP2.split(' ')

# armazenando valores nas variaveis
QNT1 = v1[1]
QNT2 = v2[1]
VL1 = v1[2]
VL2 = v2[2]

# calculo
TOTAL = (int(QNT1)*float(VL1)) + (int(QNT2)*float(VL2))

print('VALOR A PAGAR: R$ {:.2f}'.format(TOTAL))
