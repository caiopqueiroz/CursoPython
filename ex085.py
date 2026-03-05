conj = []
for cont in range(1, 8):
	valo = int(input(f'{cont}º valor: '))
	if cont == 1:
		conj.append(valo)
	else:
		if valo % 2 == 0:
			conj.insert(0, valo)
		else:
			conj.append(valo)
print(f'\n{conj}')
conj.sort()
print(f'\nVALORES PARES E ÍMPARES EM ORDEM CRESCENTE:\n {conj}')