def valinome(mens):
    while True:
        nome = input(mens).strip().title()
        if nome.isalpha():
            return nome
        else:
            print('\033[31m!ERRO! Por favor, digite um nome válido\033[m')

nome = valinome('Nome: ')
print(nome)