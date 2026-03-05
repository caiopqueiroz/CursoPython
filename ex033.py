n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
if n1 > n2 > n3:
    print(f'O maior número é {n1} e o menor é {n3}')
else:
    if n1 > n3 > n2:
        print(f'O maior número é {n1} e o menor é {n2}')
    else:
       if n2 > n3:
           print(f'O maior número é {n2} e o menor é {n1}' if n3 > n1 else print(f'O maior número é {n2} e o menor é {n3}'))
       else:
           print(f'O maior número é {n3} e o menor é {n1}' if n2 > n1 else print(f'O maior número é {n3} e o menor é {n2}'))



