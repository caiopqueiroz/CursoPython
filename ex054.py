from datetime import date
atua = date.today().year
somaa = 0
somac = 0
for cont in range(1, 8):
    nasc = int(input(f'Ano de nascimento da {cont}ª pessoa: '))
    idad = atua - nasc
    if idad >= 21:
        somaa += 1
    else:
        somac += 1
print(f'\n{somaa} dessas pessoas já são maiores de idade \n'
      f'{somac} ainda não são.')