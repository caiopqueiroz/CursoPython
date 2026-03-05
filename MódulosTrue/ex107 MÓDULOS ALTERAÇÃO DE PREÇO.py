from uteis import moeda
from uteis import numeros
from uteis import estetica


estetica.titu('== MODULARIZAÇÃO - !PREÇOS! ==')
nume = float(input('Digite um valor para ser usado como preço: '))
porc = numeros.leiaint('Digite um valor para ser usado como porcentagem: ')
estetica.linh(34)
print(f'Aumentando R${nume} em {porc}% temos {moeda.aume(nume, porc):.2f}')
print(f'Diminuindo R${nume} em {porc}% temos {moeda.dimi(nume, porc):.2f}')
print(f'O dobro de R${nume} é {moeda.dobr(nume)}')
print(f'A metade de R${nume} é {moeda.meta(nume)}')
estetica.titu('== PROGRAMA ENCERRADO ==')

