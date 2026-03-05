ret1 = float(input('Comprimento da reta 1: '))
ret2 = float(input('Reta 2: '))
ret3 = float(input('Reta 3: '))
if ret1 + ret2 > ret3 and ret1 + ret3 > ret2 and ret2 + ret3 > ret1:
	ret1 == ret2 == ret3
	cate = 'EQUILÁTERO'
	if ret1 == ret2 != ret3 or ret1 == ret3 != ret2 or ret2 == ret3 != ret1:
		cate = 'ISOSCÉLES'
	elif ret1 != ret2 != ret3:
		cate = 'ESCALENO'
	print(f'Essas três retas \033[32mPODEM\033[m formar um triângulo \033[34m{cate}\033[m!')
else:
	print('Essas três retas \033[31mNÃO PODEM\033[m formar um triângulo.')