# entrada initial hour, initial minute, final hour, final minute
entrance = input()

# extrair os valores e setar nas novas variaveis
v = entrance.split(' ')
hi = int(v[0])
mi = int(v[1])
hf = int(v[2])
mf = int(v[3])

# variaveis
rh = 0
rm = 0

# condição
# se horas iguais 24 horas
if (hi == hf) and (mi == mf):
    rh = 24
    rm = 0

# se horas iguais e minutos diferentes
elif hi == hf:
    rh = 23

    # minutos maior
    if mi > mf:
        rm = (60 - mi) + mf

    # minutos menor
    elif mi < mf:
        rm = mf - mi

# se horas diferente ( < )
elif hi < hf:

    # minutos iguais ou minutos <
    if (mi == mf) or (mi < mf):
        rh = hf - hi
        rm = mf - mi

    # minutos >
    elif mi > mf:
        rh = (hf - hi) - 1
        rm = (60 - mi) + mf

# se horas diferente ( > )
elif hi > hf:

    # minutos iguais ou minutos <
    if (mi == mf) or (mi < mf):
        rh = (24 - hi) + hf
        rm = mf - mi

    # minutos >
    elif mi > mf:
        rh = ((24 - hi) + hf) - 1
        rm = (60 - mi) + mf

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(rh, rm))
