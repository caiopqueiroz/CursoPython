print('-'*50)
print('\033[33mCálculo de IMC\033[m')
print('-'*50)
peso = float(input('Peso em kg: '))
altu = float(input('Altura em m: '))
imc = peso / (altu ** 2)
print('-'*50)
if imc < 18.5:
    situ = '\033[31mABAIXO DO PESO\033[m'
elif 18.5 <= imc < 25:
    situ = '\033[32mPESO IDEAL\033[m'
elif 25 <= imc < 30:
    situ = '\033[33mSOBREPESO\033[m'
elif 30 <= imc < 40:
    situ = '\033[31mOBESIDADE\033[m'
else:
    situ = 'OBESIDADE MÓRBIDA'
print('Muito bem! Seu IMC é {:.1f} \n Isso significa que sua situação atual é: {}'.format(imc, situ))
