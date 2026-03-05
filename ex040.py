not1 = float(input('Nota 1 (0 a 10): '))
not2 = float(input('Nota 2 (0 a 10): '))
medi = (not1 + not2) / 2
if not1 > 10 and not2 > 10 or medi > 10:
    print('\033[31mAlgo errado.\033[m')
else:
    if medi < 5:
        situ = '\033[31mREPROVADO\033[m'
    elif 5 <= medi <= 6.9:
        situ = '\033[33mEM RECUPERAÇÃO\033[m'
    elif 10 >= medi > 6.9:
        situ = '\033[32mAPROVADO\033[m'
    print('Média final: {:.2f} \n '
          'Sua situação atual é: {}'.format(medi, situ))
