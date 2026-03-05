list0 = []
list1 = []
list2 = []
matr = []
for cont in range(0, 9):
	valo = int(input('Valor: '))
	if cont == 0 or cont == 1 or cont == 2:
		list0.append(valo)
	if cont == 3 or cont == 4 or cont == 5:
		list1.append(valo)
	if cont == 6 or cont == 7 or cont == 8:
		list2.append(valo)
matr.append(list0[:])
matr.append(list1[:])
matr.append(list2[:])
print(f'\n{matr[0]}\n{matr[1]}\n{matr[2]}')