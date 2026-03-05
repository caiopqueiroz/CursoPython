a1 = float(input('Primeiro termo da P.A.: '))
raza = float(input('Razão: '))
print('\033[;7m Os 10 primeiros termos dessa P.A. são: \033[m')
sequ = 1
while sequ < 11:
    print(f'{sequ}º -> {a1 + (raza * sequ) - raza:.1f}')
    sequ += 1
mais = int(input('Quantos termos mais você gostaria de ver? \033[31m(Digite 0 para encerrar o programa)\033[m '))
while mais != 0:
    apoi = sequ
    while sequ < apoi + mais:
        print(f'{sequ}º -> {a1 + (raza * sequ) - raza:.1f}')
        sequ += 1
    mais = int(input('Quantos termos mais você gostaria de ver? \033[31m(Digite 0 para encerrar o programa)\033[m '))
if mais == 0:
    print('\n Fim')