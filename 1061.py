# entrada dia 1
di = str(input())

# extrair valor dia 1
v = di.split(' ')
di = int(v[1])

# entrada hi, mi e si
hi, mi, si = map(int, input().split(' : '))

# entrada dia final
df = str(input())

# extrair valor dia final
v = df.split(' ')
df = int(v[1])

# entrada hf, mf e sf
hf, mf, sf = map(int, input().split(' : '))

# se segundos si e sf menor ou iguais
if si <= sf:
    st = sf - si

    # se minutos iguais ou mi < mf
    if mi <= mf:
        mt = mf - mi

        # se horas iguais ou hi < hf
        if hi <= hf:
            ht = hf - hi
            dt = df - di

        # se hi > hf
        elif hi > hf:
            ht = (24 - hi) + hf
            dt = (df - di) - 1

    # minutos mi > mf
    elif mi > mf:
        mt = (60 - mi) + mf

        # se horas iguais ou hi < hf
        if hi <= hf:
            ht = (hf - hi) - 1
            dt = (df - di) - 1

            if ht < 0:
                ht = 24 + ht

        # se hi > hf
        elif hi > hf:
            ht = ((24 - hi) + hf) - 1
            dt = (df - di) - 1

# se segundos si > sf
elif si > sf:
    st = (60 - si) + sf

    # se minutos mi <= mf
    if mi <= mf:
        mt = (mf - mi) - 1

        if mt < 0:
            mt = 60 + mt

            # se horas iguais ou hi < hf
            if hi <= hf:
                ht = (hf - hi) - 1

                if ht < 0:
                    ht = 24 + ht
                    dt = (df - di) - 1

                elif ht == 0:
                    ht = 0
                    dt = df - di

            # se hi > hf
            elif hi > hf:
                ht = ((24 - hi) + hf) - 1
                dt = (df - di) - 1

        # minutos = 0
        elif mt == 0:

            # se horas iguais
            if hi == hf:
                ht = hf - hi
                dt = df - di

    # se minutos mi > mf
    elif mi > mf:
        mt = ((60 - mi) + mf) - 1

        # horas <=
        if hi <= hf:
            ht = 24 + ((hf - hi) - 1)

            if ht == 24:
                ht = 0
                dt = df - di

            else:
                dt = (df - di) - 1

        # horas hi > hf
        elif hi > hf:
            ht = ((24 - hi) + hf) - 1
            dt = (df - di) - 1

print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dt, ht, mt, st))
