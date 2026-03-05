import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hip = math.sqrt(co**2 + ca**2)
print('A hipotenusa desse triângulo é igual à: {:^2.3f}'.format(hip))