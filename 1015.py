from math import sqrt

# entrada
p1 = input()
p2 = input()

# extraindo valores
v1 = p1.split(' ')
v2 = p2.split(' ')

# armazenando valores
p1x1 = float(v1[0])
p1y1 = float(v1[1])
p2x2 = float(v2[0])
p2y2 = float(v2[1])

# calculo
distance = sqrt(((p2x2 * p2x2) - (2 * p2x2 * p1x1) + (p1x1 * p1x1)) + ((p2y2 * p2y2) - (2 * p2y2 * p1y1) + (p1y1 * p1y1)))

print('{:.4f}'.format(distance))
