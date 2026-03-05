valo = list()
cont = 1
while True:
	nume = int(input(f'\n{cont}º valor: '))
	if nume not in valo:
		valo.append(nume)
	else:
		print('\033[31m!ESSE NÚMERO JÁ FOI INSERIDO!\033[m')
	cont += 1
	coma = str(input('\033[31mPARAR? \033[m')).strip().upper()
	if coma == 'S' or coma == 'SIM':
		break
valo.sort()
print('\nEssa é a lista dos valores digitados em \033[33mordem crescente\033[m: \n \n',
      valo)