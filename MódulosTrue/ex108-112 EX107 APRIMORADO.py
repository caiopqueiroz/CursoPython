from uteis import numeros
from uteis import moeda
from uteis import estetica
from uteis import dado


estetica.titu('== PYTHON MANIPULADOR DE PREÇO 1.5 ==')
nume = dado.leiadinh('Digite o preço: R$')
porcaume = numeros.leiaint('Porcentagem de aumento: ')
porcdimi = numeros.leiaint('Porcentagem de diminuição: ')
moeda.resu(nume, porcaume, porcdimi)
estetica.titu('== PROGRAMA ENCERRADO ==')