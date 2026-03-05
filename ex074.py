from random import randint
import math
conj = (randint(1, 10), randint(1, 10), randint(1,10), randint(1,10), randint(1,10))
print('Os números que sorteei foram: ', end='')
for apoi in conj:
    print(apoi, end=' ')
print(f'\n \n O maior número é o {max(conj)}')
print(f' O menor número é o {min(conj)}')




