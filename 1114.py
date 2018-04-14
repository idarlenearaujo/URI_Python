# variaveis
password = False
cPassword = 2002

# entrada dos numeros
while password is False:
    number = int(input())

    if number != cPassword:
        print('Senha Invalida')
    else:
        print('Acesso Permitido')
        break
