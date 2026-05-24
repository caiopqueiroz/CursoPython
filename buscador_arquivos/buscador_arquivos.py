caminhos = ['buscador_arquivos/teste.txt', 'buscador_arquivos/outro_teste.txt', '../VisualizaçãoDados/Linguagem R.txt', '../../Caio/Ideias/Buscador de arquivos.txt']
encontrou = False
escrever_frase = False
fim_linha = True
ultima_linha = False
linhas_arquivos = list()
contador = 0
contador_arquivo = -1
print('Buscador de arquivos\n')
comando = str(input('Digite a palavra que deseja buscar: '))
for elemento in caminhos:
    caminho = elemento
    arquivo = open(caminho, 'rt', encoding='utf-8')
    titulo = caminho.split('/')
    
    for elemento in titulo:
        if comando in elemento:
            print(f'\nExiste um arquivo com esse nome - \033[34m{caminho}\033[m')

for elemento in caminhos:
    caminho = elemento
    arquivo = open(caminho, 'rt', encoding='utf-8')
    contador_linhas = 0
    linha_atual = 0

    for linha in arquivo:
        contador_linhas += 1

    linhas_arquivos.append(contador_linhas)

for elemento in caminhos:
    caminho = elemento
    arquivo = open(caminho, 'rt', encoding='utf-8')
    contador_arquivo += 1
    linha_atual = 0

    for linha in arquivo:
        linha_atual += 1
        if linha_atual == linhas_arquivos[contador_arquivo]:
            ultima_linha = True
        else:
            ultima_linha = False
        palavras = linha.split(' ')
        contador_palavras = 0

        for palavra in palavras:
            if palavra == '\n':
                palavras.remove(palavra)

            if '\n' in palavra:
                if palavra in palavras:
                    palavra_corrigida = palavra.split('\n')
                    palavras.remove(palavra)
                    palavras.append(palavra_corrigida[0])        
        
        for palavra in palavras:
            contador_palavras += 1

            if comando in palavra:
                frase = list()
                contador = 0
                escrever_frase = True
                encontrou = True
                fim_linha = False
                local = caminho
                print(f'\nEncontrei essa palavra no arquivo \033[32m{caminho}\033[m')
            
            if not fim_linha:
                if escrever_frase:
                    if contador <= 5:
                        frase.append(palavra)
                        contador += 1

            if contador_palavras == len(palavras):
                if ultima_linha == True:
                    fim_linha = True
                    if escrever_frase:
                        print('Prévia: ', end='')
                        for elemento in frase:
                            print(f'\033[7;2m{elemento} \033[m', end='')
                        print()
                        escrever_frase = False
            if contador > 5:
                fim_linha = True
                if escrever_frase:
                    print('Prévia: ', end='')
                    for elemento in frase:
                        print(f'\033[7;2m{elemento} \033[m', end='')
                    print()
                    escrever_frase = False

if not encontrou:
    print('\n\033[31mNão encontrei essa palavra em nenhum arquivo\033[m')
