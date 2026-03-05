n = input('Nome completo: ')
print('TODAS AS LETRAS MAIÚSCULAS:', n.upper())

print('todas as letras minúsculas:', n.lower())

x = n.split()
y = ''.join(x)
print('Total de caracteres:', len(y))

print('Total de caracteres do primeiro nome:', len(x[0]))