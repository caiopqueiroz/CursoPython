def leiaint(fras):
    while True:
        n = input(fras)
        if n.isnumeric():
            n = int(n)
            return n
        else:
            print('\033[31m!ERRO! Por favor digite um número inteiro positivo\033[m')


nume = leiaint('Digite um número: ')
print(f'O número digitado foi {nume}')

