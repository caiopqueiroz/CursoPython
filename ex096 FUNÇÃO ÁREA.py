def area(larg, comp):
    print(f'{larg} x {comp} = {larg * comp:.2f} m^2')
def apre(titu):
    print(f'-' * (len(titu) + 2))
    print(f' {titu}')
    print(f'-' * (len(titu) + 2))


apre('== CÁLCULO DA ÁREA DO TERRENO ==')
while True:
    larg = float(input('Largura em m: '))
    comp = float(input('Comprimento em m: '))
    area(larg, comp)
    print()
    while True:
        coma = str(input('Deseja encerrar o programa? (S/N) ')).upper().strip()[0]
        if coma not in 'SN':
            print('\033[31mERRO\033[m')
        else:
            break
    print()
    if coma in 'S':
        break
print('== PROGRAMA ENCERRADO ==')

