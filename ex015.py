km = float(input('Quantos km seu carro alugado andou? '))
d = int(input('Além disso, durante quantos dias ele andou? '))
x = 60*d
y = 0.15*km
print('O valor total que isso te custou foi R${:.2f}'.format(x+y))
