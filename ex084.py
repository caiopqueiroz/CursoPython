pess = []
conjpess = []
contpess = 0

nomemaio = ''
pesomaio = 0
pesa = []
conjpesa = []

nomemeno = ''
pesomeno = 0
leve = []
conjleve = []

while True:
    nome = str(input('\nNome: ')).strip().title()  # DECLARANDO NOME E PESO
    peso = int(input('Peso em kg: '))

    pess.append(nome)  # COLOCANDO AMBOS NA LISTA INDIVIDUAL DE PESSOAS
    pess.append(peso)

    if contpess == 0:  # SE O CONTADOR AINDA FOR IGUAL A 0
        nomemaio = nome  # NOME E PESO SERÃO CONSIDERADOS COMO OS DA PESSOA MAIS PESADA
        pesomaio = peso

        pesa.append(nomemaio)  # SERÃO ADICIONADOS NA LISTA PROVISÓRIA QUE GUARDA O INDIVÍDUO MAIS PESADO
        pesa.append(pesomaio)

        conjpesa.append(pesa[:])  # UMA CÓPIA SERÁ ADICIONADA À LISTA DEFINITIVA

        pesa.clear()  # LISTA PROVISÓRIA RESETADA

        nomemeno = nome
        pesomeno = peso

        leve.append(nomemeno)
        leve.append(pesomeno)

        conjleve.append(leve[:])

        leve.clear()

    else:  # SE FOR O CADASTRO DA SEGUNDA PESSOA EM DIANTE
        if peso > pesomaio:  # SE O PESO DA PESSOA CADASTRADA DA VEZ FOR MAIOR QUE O MAIOR PESO CADASTRADO ATÉ ENTÃO
            conjpesa.clear()  # RESET DA LISTA DEFINITIVA POIS A PESSOA CONTIDA NELA NÃO É MAIS A MAIS PESADA

            nomemaio = nome  # O NOME E PESO SERÃO AGORA CONSIDERADOS COMO OS DA PESSOA MAIS PESADA
            pesomaio = peso

            pesa.append(nomemaio)  # SERÃO ADICIONADOS À LISTA PROVISÓRIA
            pesa.append(pesomaio)

            conjpesa.append(pesa[:])  # E À LISTA DEFINITIVA

            pesa.clear()  # LISTA PROVISÓRIA RESETADA

        if peso == pesomaio and nome != nomemaio:  # SE O PESO DA PESSOA CADASTRADA DA VEZ FOR IGUAL AO MAIOR PESO CADASTRADO ATÉ ENTÃO
            nomemaio = nome  # O NOME DA PESSOA MAIS PESADA PASSARÁ A SER O NOVO

            pesa.append(nomemaio)  # SERÃO ADICIONADOS Á LISTA PROVISÓRIA
            pesa.append(pesomaio)

            conjpesa.append(pesa[:])  # TAMBÉM À LISTA DEFINITIVA, SEM EXCLUIR OS DADOS QUE JÁ ESTÃO LÁ

            pesa.clear()  # LISTA PROVISÓRIA RESETADA

        if peso < pesomeno:
            conjleve.clear()

            nomemeno = nome
            pesomeno = peso

            leve.append(nomemeno)
            leve.append(pesomeno)

            conjleve.append(leve[:])

            leve.clear()

        if peso == pesomeno and nome != nomemeno:
            nomemeno = nome

            leve.append(nomemeno)
            leve.append(pesomeno)

            conjleve.append(leve[:])

            leve.clear()

    conjpess.append(pess[:])  # COLOCANDO UMA CÓPIA DAS INFORMAÇÕES DE 1 INDIVÍDUO NA LISTA COM TODOS OS INDIVÍDUOS

    pess.clear()  # RESETANDO A LISTA INDIVIDUAL

    contpess += 1

    coma = str(input('PARAR? ')).upper().strip()  # COMANDO DE INTERRUPÇÃO DO LOOPING
    if 'SIM' in coma or 'S' in coma:
        break

print(f'\n\033[33;7;1m {contpess} pessoas cadastradas. \033[m')

print('\nLISTA DAS PESSOAS MAIS PESADAS')
for pess in conjpesa:  # MOSTRANDO A LISTA FORMATADA E ORGANIZADA DE TODAS AS PESSOAS COM O MAIOR PESO
    print(f' \033[34m{pess[0]}\033[m pesa \033[34m{pess[1]}\033[m kg')

print('\nLISTA DAS PESSOAS MAIS LEVES')
for pess in conjleve:
    print(f' \033[35m{pess[0]}\033[m pesa \033[35m{pess[1]}\033[m kg ')






