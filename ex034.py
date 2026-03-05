sala = float(input('Valor do salário atual: '))
if sala > 1250:
    aume = 10/100 * sala
    nsala = aume + sala
    print('PARABÉNS! Você vai receber um aumento de R${:.2f} \n Seu novo salário será R${:.2f}'.format(aume, nsala))
else:
    aume = 15/100 * sala
    nsala = aume + sala
    print('PARABÉNS! Você vai receber um aumento de R${:.2f} \n Seu novo salário será R${:.2f}'.format(aume, nsala))