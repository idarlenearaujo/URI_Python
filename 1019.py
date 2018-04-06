#entrada
timeSegundos = int(input())

#variaveis
horas = 0
minutos = 0
segundos = 0

#saber quantos minutos/horas há
minutos = timeSegundos // 60

#se minutos superarem 60 minutos
if minutos >= 60:

    #calculo horas se maior que  60
    horas = minutos // 60

    #segundos restantes
    timeSegundos = timeSegundos - (horas * 60 * 60)

    #calculo dos minutos
    minutos = timeSegundos // 60

    #calculo dos segundos
    segundos = timeSegundos - (minutos * 60)

else:
    #calculo segundos
    segundos = timeSegundos - (minutos * 60)

print('{}:{}:{}'.format(horas, minutos, segundos))