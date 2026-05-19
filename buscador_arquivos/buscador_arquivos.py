caminhos = ['buscador_arquivos/teste.txt', 'buscador_arquivos/outro_teste.txt', '../VisualizaçãoDados/Linguagem R.txt']
encontrou = False
print('Buscador de arquivos')
comando = str(input('Digite a palavra que deseja buscar: '))
for elemento in caminhos:
    caminho = elemento
    arquivo = open(caminho, 'rt')
    titulo = caminho.split('/')
    
    for elemento in titulo:
        if comando in elemento:
            print(f'\nExiste um arquivo com esse nome - \033[34m{caminho}\033[m')

    for linha in arquivo:
        palavras = linha.split(' ')
        for palavra in palavras:
            if comando in palavra:
                encontrou = True
                local = caminho
                print(f'\nEncontrei essa palavra no arquivo \033[32m{caminho}\033[m')
if not encontrou:
    print('\n\033[31mNão encontrei essa palavra em nenhum arquivo\033[m')
