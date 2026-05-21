caminhos = ['buscador_arquivos/teste.txt']
encontrou = False
escrever_frase = False
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
    titulo = caminho.split('/')
    
    for linha in arquivo:
        palavras = linha.split(' ')
        
        for palavra in palavras:
            if palavra == '\n':
                palavras.remove(palavra)

            if '\n' in palavra:
                if palavra in palavras:
                    palavra_corrigida = palavra.split('\n')
                    palavras.remove(palavra)
                    palavras.append(palavra_corrigida[0])
        
        if len(palavras) == 0:
            del palavras
        else:
            print(palavras)