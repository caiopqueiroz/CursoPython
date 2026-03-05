a1 = int(input('Primeiro termo da P.A.: '))
raza = int(input('Razão: '))
print('\033[1;7m Os 10 primeiros termos dessa P.A. são: \033[m')
for sequ in range(1, 11):
	print(f'{sequ}º = {a1 + (raza * sequ) - raza}')