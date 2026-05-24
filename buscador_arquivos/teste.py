#caminhos = ['buscador_arquivos/teste.txt', 'buscador_arquivos/outro_teste.txt', '../VisualizaçãoDados/Linguagem R.txt', '../../Caio/Ideias/Buscador de arquivos.txt']
caminhos = ['buscador_arquivos/teste.txt', 'buscador_arquivos/outro_teste.txt']
encontrou = False
escrever_frase = False
fim_linha = True
ultima_linha = False
linhas_arquivos = list()
contador = 0
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
print(linhas_arquivos)