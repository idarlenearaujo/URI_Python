# entrada de 1 string e 2 float
name = str(input())
salario = float(input())
totalvendido = float(input())

# variavel
comissao = 0.15

# calculo
salarioFinal = salario + (totalvendido * comissao)

print('TOTAL = R$ {:.2f}'.format(salarioFinal))
