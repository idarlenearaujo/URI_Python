# entrada float
value = float(input())

# variaveel
cashier = True
qnt100 = 0
qnt50 = 0
qnt20 = 0
qnt10 = 0
qnt5 = 0
qnt2 = 0
qnt1 = 0
qnt05 = 0
qnt025 = 0
qnt010 = 0
qnt005 = 0
qnt001 = 0

while cashier is True:

    if value >= 100:
        qnt100 = value // 100
        value = value - (qnt100 * 100)

        value = "%.2f" % value
        value = float(value)

    elif value >= 50:
        qnt50 = value // 50
        value = value - (qnt50 * 50)

        value = "%.2f" % value
        value = float(value)

    elif value >= 20:
        qnt20 = value // 20
        value = value - (qnt20 * 20)

        value = "%.2f" % value
        value = float(value)

    elif value >= 10:
        qnt10 = value // 10
        value = value - (qnt10 * 10)

        value = "%.2f" % value
        value = float(value)

    elif value >= 5:
        qnt5 = value // 5
        value = value - (qnt5 * 5)

        value = "%.2f" % value
        value = float(value)

    elif value >= 2:
        qnt2 = value // 2
        value = value - (qnt2 * 2)

        value = "%.2f" % value
        value = float(value)

    elif value >= 1:
        qnt1 = value // 1
        value = value - (qnt1 * 1)

        value = "%.2f" % value
        value = float(value)

    elif value >= 0.50:
        qnt05 = value // 0.5
        value = value - (qnt05 * 0.5)

        value = "%.2f" % value
        value = float(value)

    elif value >= 0.25:
        qnt025 = value // 0.25
        value = value - (qnt025 * 0.25)

        value = "%.2f" % value
        value = float(value)

    elif value >= 0.10:
        qnt010 = value // 0.10
        value = value - (qnt010 * 0.10)

        value = "%.2f" % value
        value = float(value)

    elif value >= 0.05:
        qnt005 = value // 0.05
        value = value - (qnt005 * 0.05)

        value = "%.2f" % value
        value = float(value)

    elif value >= 0.01:
        qnt001 = value / 0.01
        value = value - (qnt001 * 0.01)

        value = "%.2f" % value
        value = float(value)

    elif value == 0.00:

        cashier = False

print('NOTAS:\n'
      '{} nota(s) de R$ 100.00\n'
      '{} nota(s) de R$ 50.00\n'
      '{} nota(s) de R$ 20.00\n'
      '{} nota(s) de R$ 10.00\n'
      '{} nota(s) de R$ 5.00\n'
      '{} nota(s) de R$ 2.00\n'
      'MOEDAS:\n'
      '{} moeda(s) de R$ 1.00\n'
      '{} moeda(s) de R$ 0.50\n'
      '{} moeda(s) de R$ 0.25\n'
      '{} moeda(s) de R$ 0.10\n'
      '{} moeda(s) de R$ 0.05\n'
      '{} moeda(s) de R$ 0.01'
      .format(int(qnt100), int(qnt50), int(qnt20), int(qnt10), int(qnt5), int(qnt2), int(qnt1), int(qnt05), int(qnt025), int(qnt010), int(qnt005), int(qnt001)))
