# entrada salario atual
salary = float(input())

# variavel
r = 0
p = 0

# condição
# salario 0 - 400 (15%)
if 0 <= salary <= 400:
    p = 15
    r = salary * (p/100)

# salario 400.01 - 800 (12%)
elif 400.01 <= salary <= 800:
    p = 12
    r = salary * (p/100)

# salario 800.01 - 1200 (10%)
elif 800.01 <= salary <= 1200:
    p = 10
    r = salary * (p / 100)

# salario 1200.01 - 2000 (7%)
elif 1200.01 <= salary <= 2000:
    p = 7
    r = salary * (p / 100)

# salario 2000.01 - > (4%)
elif salary >= 2000.01:
    p = 4
    r = salary * (p / 100)

# novo salario
salary = salary + r

print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %'.format(salary, r, p))
