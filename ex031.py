dist = float(input('Distância em km: '))
if dist <= 200:
    prec = dist * 0.5
    print(f'O preço da passagem é R${prec:.2f}')
else:
    prec = dist * 0.45
    print(f'O preço da passagem é R${prec:.2f}')
