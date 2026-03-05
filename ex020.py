from random import shuffle
n1 = input('Nome 1: ')
n2 = input('Nome 2: ')
n3 = input('Nome 3: ')
n4 = input('Nome 4: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será: {} '.format(lista))
