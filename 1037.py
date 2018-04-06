# entrada
number = float(input())

# condição 1
if (number >= 0) and (number <= 25):
    print('Intervalo [0,25]')

# condição 2
elif (number > 25) and (number <= 50):
    print('Intervalo (25,50]')

# condição 3
elif (number > 50) and (number <=75):
    print('Intervalo (50,75]')

# condição 4
elif (number > 75) and (number <= 100):
    print('Intervalo (75,100]')

# condição 5
elif (number < 0) or (number > 100):
    print('Fora de intervalo')
