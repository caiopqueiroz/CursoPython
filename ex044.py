valo = float(input('Valor do produto: R$'))
print('Possíveis formas de pagamento: \n'
      '\033[34m1)\033[m À VISTA (DINHEIRO OU CHEQUE) \033[32m!10% DE DESCONTO!\033[m \n'
      '\033[34m2)\033[m À VISTA (CARTÃO) \033[32m!5% DE DESCONTO!\033[m \n'
      '\033[34m3)\033[m 2x NO CARTÃO \033[32m!SEM JUROS!\033[m \n'
      '\033[34m4)\033[m 3x OU MAIS NO CARTÃO \033[32m!20% DE JUROS!\033[m')
esco = int(input('Digite aqui o número correspondente á sua escolha: '))
if esco == 1:
    tota = valo * 90/100
    nparc = 1
    parc = tota
elif esco == 2:
    tota = valo * 95/100
    nparc = 1
    parc = tota
elif esco == 3:
    parc = valo / 2
    tota = valo
    nparc = 2
elif esco == 4:
    nparc = int(input('Qual o número de parcelas desejado? \033[33m(máx 12)\033[m '))
    tota = 120/100 * valo
    parc = tota / nparc
print('Você pagará o VALOR TOTAL de \033[34mR${:.2f}\033[m pelo produto dividido em APENAS \033[34m{}\033[m PARCELA(S) \n'
      'VALOR FINAL DA(S) PARCELA(S): \033[34mR${:.2f}\033[m'.format(tota, nparc, parc))
