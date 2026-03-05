a1 = float(input('Primeiro termo da P.A.: '))
raza = float(input('Razão: '))
print('\033[;7m Os 10 primeiros termos dessa P.A. são: \033[m')
sequ = 1
while sequ < 11:
    print(f'{sequ}º -> {a1 + (raza * sequ) - raza}')
    sequ += 1