indi = []
diar = []
indibole = []
bole = []
iden = 0
while True:
    nome = str(input(f'\nNome do aluno {iden}: ')).strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    medi = (nota1 + nota2) / 2
    indibole.append(nome)
    indibole.append(medi)
    bole.append(indibole[:])
    indibole.clear()
    indi.append(nome)
    indi.append(nota1)
    indi.append(nota2)
    diar.append(indi[:])
    indi.clear()
    iden += 1
    coma1 = str(input('\033[31mPARAR?\033[m ')).upper().strip()
    if coma1 in 'SIM':
        break
print('\n')
idenapoi = 0
for indibole in bole:
    print(f'Aluno \033[1m{idenapoi}\033[m: \033[34;7;1m {indibole[0]} \033[m   Média: \033[33;7;1m {indibole[1]:.1f} \033[m\n')
    idenapoi += 1
print('\nCaso queira consultar as notas de um aluno específico')
while True:
    resp = int(input('\n\033[33mDigite aqui o número correspondente:\033[m '))
    if resp <= idenapoi - 1:
        print(f'Aluno \033[1m{resp}\033[m: \033[34;7;1m {diar[resp][0]} \033[m  Nota 1: \033[33;7;1m {diar[resp][1]} \033[m  Nota 2: \033[33;7;1m {diar[resp][2]} \033[m')
    else:
        print('\033[31mEsse aluno não existe.\033[m')
    coma2 = str(input('\033[31mPARAR?\033[m ')).upper().strip()
    if coma2 in 'SIM':
        break