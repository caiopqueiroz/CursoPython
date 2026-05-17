caminho = 'buscador_arquivos/teste.txt'
print('Buscador de arquivos')
comando = str(input('Digite a palavra que deseja buscar: '))
resultado = 'Não encontrei'
arquivo = open(caminho, 'rt')
# para cada linha no arquivo
for linha in arquivo:
    # criando uma lista de palavras presentes na linha
    palavras = linha.split(' ')
    # para cada palvra nessa lista de palavras
    for palavra in palavras:
        # se o comando for a palavra 
        if comando in palavra:
            resultado = 'Encontrei'
print(resultado)

    






# caneta = open(arquivo, 'at')
#caneta.write(palavra)
