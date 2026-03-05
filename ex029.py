veloc = int(input('Velocidade do carro em km/h: '))
if veloc > 80:
    exce = veloc - 80
    mult = (veloc - 80) * 7
    print('Excedeu o limite de velocidade em {} km/h \n Sua multa será R${:.2f}'.format(exce, mult))
else:
    print('Continue dirigindo com cuidado!')