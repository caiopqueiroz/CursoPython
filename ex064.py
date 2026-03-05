print('Bem-vindo(a)! Aqui, você poderá digitar quantos valores quiser. \n'
      'Quando quiser parar, basta digitar \033[31m999\033[m')
nume = 0
quan = 0
apoi = nume
while nume != 999:
    nume = int(input('\n Digite um número inteiro: '))
    apoi += nume
    quan += 1
print('\n Estatísticas finais:  ')
print('Quantos números você digitou? ', '\033[34;7;1m', quan - 1, '\033[m')
print('Qual a somatória deles? ', '\033[34;7;1m', apoi - 999, '\033[m')