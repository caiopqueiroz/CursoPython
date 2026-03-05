cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
        'dezoito', 'dezenove', 'vinte')

nume = int(input('Digite um número de 0 a 20: '))

if 20 >= nume >= 0:
    print(f'Você digitou o número \033[33;7;1m {cont[nume].title()} \033[m')

else:
    while True:
        print('\033[31mAlgo errado.\033[m')
        nume = int(input('Digite um número de 0 a 20: '))
        if 20 >= nume >= 0:
            print(f'Você digitou o número \033[33;7;1m {cont[nume].title()} \033[m')
            break

