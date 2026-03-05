from uteis import estetica
from uteis import numeros


estetica.linh(60)
valo = numeros.leiaint('Digite um valor inteiro:    ')
valo2 = numeros.leiafloa('   Digite um valor real:    ')
estetica.linh(60)
print(f'Valor inteiro digitado: \t{valo}\n'
      f'   Valor real digitado: \t{valo2}'.replace('.', ','))
estetica.linh(60)
print('\033[31m== PROGRAMA ENCERRADO ==\033[m')
estetica.linh(60)

