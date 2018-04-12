# entrada numero
number = int(input())

# teste de 1 - 10000 quais que se dividos por number resta 2
for i in range(1, 10001):
    if i % number == 2:
        print(i)
