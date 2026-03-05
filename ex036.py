casa = float(input('Valor da casa: '))
sala = float(input('Salário do comprador: '))
anos = int(input('Tempo total do pagamento (em anos): '))
exce = 30/100 * sala
pres = (casa / anos) / 12
if pres > exce:
    print('Me desculpe, mas o valor R${:.2f} da prestação excedeu 30% do seu salário de R${:.2f}. \n'
          '\033[31mO empréstimo foi negado\033[m.'.format(pres, sala))
elif exce > pres:
    print('\033[32mParabéns! Seu empréstimo foi aceito\033[m. O valor da sua prestação será R${:.2f}'.format(pres))