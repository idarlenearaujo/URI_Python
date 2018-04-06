#entrada
Edays = int(input())

#variavel
days = 0
month = 0
year = 0

#definido quantidade de meses
month = Edays // 30

#condição se meses maior ou igual a 12
if month >= 12:

    #calculo de anos
    year = Edays // 365

    #dias restantes
    Edays = Edays - (year * 365)

    #calculo mês
    month = Edays // 30

    #dias restantes
    days = Edays - (month * 30)
else:

    #dias restantes
    days = Edays - (month * 30)

print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(year, month, days))
