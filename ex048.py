soma = 0
for cont in range(3, 500, 2):
    if cont % 3 == 0:
        soma += cont
print(f'A \033[7:1m SOMA \033[m de todos os números \033[33mímpares\033[m e \033[33mmúltiplos de 3\033[m entre 1 e 500 é: \033[1:7m {soma} \033[m')

