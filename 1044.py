# entrada
entrance = input()

# extrair 2 valores inteiros
v = entrance.split(' ')
A = int(v[0])
B = int(v[1])

# condição se multiplo ou não
if ((B % A) == 0) or ((A % B) == 0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
