somaidad = 0
velh = 0
somamulh = 0
medi = 0
nomevelh = '\033[31mNÃO HÁ HOMENS\033[m'
print('\033[1;7m !!SUPER ANALISADOR EXTREMAMENTE ESPECÍFICO!! \033[m \n')
for anal in range(1, 5):
    print(f'\033[34mAnálise da {anal}ª pessoa\033[m')
    nome = str(input('Nome: ')).strip().title()
    idad = int(input('Idade: '))
    sexo = str(input('Sexo (M ou F): ')).strip().title()
    print('\n')
    somaidad += idad
    medi = somaidad / 4
    if anal == 1 and sexo == 'M':
        velh = idad
        nomevelh = nome
    else:
        if idad >= velh and sexo == 'M':
            velh = idad
            nomevelh = nome
    if idad < 20 and sexo == 'F':
        somamulh += 1
print('-'*50)
print(f'Média das idades de \033[32mTODOS\033[m: \033[1;7m {medi:.1f} \033[m \n'
      f'Nome do \033[34mHOMEM\033[m mais velho: \033[1;7m {nomevelh} \033[m \n'
      f'Quantidade de \033[35mMULHERES\033[m com menos de 20 anos: \033[1;7m {somamulh} \033[m')
