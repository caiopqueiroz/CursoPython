cate = '\033[32mÉ PRIMO\033[m'
print('\033[1;7m !!VERFICADOR DE NÚMEROS PRIMOS!! \033[m')
nume = int(input('Digite aqui um número inteiro: '))
for alca in range(1, nume + 1):
    if nume % alca == 0 and alca != nume and alca != 1:
        cate = '\033[31mNÃO É PRIMO\033[m'
    elif nume == 1:
        cate = '\033[31mNÃO É PRIMO\033[m'
print(cate)


