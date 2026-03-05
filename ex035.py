r1 = int(input('Comprimento da reta 1: '))
r2 = int(input('Comprimento da reta 2: '))
r3 = int(input('Comprimento da reta 3: '))
if r1 + r2 > r3:
    if r1 + r3 > r2:
        if r2 + r3 > r1:
            print('Essas retas \033[32mpodem\033[m formar um triângulo!')
        else:
            print('Essas retas \033[31mNÃO podem\033[m formar um triãngulo')
    else:
        print('Essas retas \033[31mNÃO podem\033[m formar um triãngulo')
else:
    print('Essas retas \033[31mNÃO podem\033[m formar um triãngulo')

