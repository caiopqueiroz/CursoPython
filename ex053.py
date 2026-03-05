print('\033[1;7m SUA FRASE É OU NÃO UM PALINDROMO? \033[m')
print('\033[34mPalindromo é toda palavra ou frase que, \n'
      'quando invertida, fica exatamente igual à original.\033[m')
fras = str(input('Digite uma frase qualquer: ')).strip().upper()
sepa = fras.split()
junt = ''.join(sepa)
inve = ''
for anal in range(len(junt) -1, -1, -1):
    inve += junt[anal]
if inve == junt:
    print(junt, '//', inve, '-> \033[32mÉ UM PALINDROMO\033[m')
else:
    print(junt, '//', inve, '-> \033[31mNÃO É UM PALINDROMO\033[m')

