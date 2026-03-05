val1 = int(input('Primeiro número inteiro: '))
val2 = int(input('Segundo número inteiro: '))
if val1 > val2:
    print(f'O \033[34mprimeiro valor\033[m é o maior!')
elif val2 > val1:
    print(f'O \033[34msegundo valor\033[m é o maior!')
else:
    print('\033[31mNão existe valor maior. Ambos são iguais\033[m.')

