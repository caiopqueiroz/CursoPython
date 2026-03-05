pare = 0
impa = 0
from time import sleep
print('\033[7;1m !!CALCULADORA DA SOMA DE NÚMEROS PARES e ÍMPARES!! \033[m')
sleep(0.5)
for inte in range(1, 7):
    valo = int(input('Número inteiro: '))
    if valo % 2 == 0:
        pare += valo
    else:
        impa += valo
sleep(0.5)
print(f'A soma de todos os valores \033[34mPARES\033[m é: {pare} \n'
      f'E a soma de todos os valores \033[33mÍMPARES\033[m é: {impa}')