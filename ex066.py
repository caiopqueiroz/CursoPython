soma = nume = cont = 0
print('Bem-vindo(a)! Aqui, você poderá digitar quantos números quiser. \n Quando quiser parar, basta escrever \033[31;1;7m 999 \033[m')
while True:
    nume = int(input('\n Digite um valor inteiro: '))
    if nume == 999:
        break
    soma += nume
    cont += 1
print(f'\n Foram digitados \033[34;7;1m {cont} \033[m números \n A soma de todos eles vale \033[34;1;7m {soma} \033[m')