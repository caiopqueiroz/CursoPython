cont = 1
apoi = 1
contmaio = 0
conthome = 0
contmulh = 0

while True:

	idad = int(input(f'\n Idade da {cont}º pessoa: '))

	sexo = str(input(f' Sexo da {cont}º pessoa: (M ou F) ')).strip().upper()

	if idad > 18:
		contmaio += 1

	if sexo == 'M':
		conthome += 1

	if sexo == 'F' and idad < 20:
		contmulh += 1

	cont += 1

	coma = int(input(' \n [ 0 ] \033[32mSIM\033[m \n [ 1 ] \033[31mNÃO\033[m \n \n \033[33mQuer continuar?\033[m '))

	if coma == 1:
		break

	elif coma == 0:
		True

	else:
		apoi = 0
		print('\n \033[31;7;1m Algo errado. \033[m')
		break

if apoi != 0:
	print(f'\n \033[33;7;1m {contmaio} pessoa(s) \033[m cadastrada(s) têm mais de 18 anos \n \n'
              f' Foram cadastrados \033[34;7;1m {conthome} homens \033[m \n \n'
              f' \033[35;7;1m {contmulh} mulher(es) \033[m cadastrada(s) têm menos de 20 anos')